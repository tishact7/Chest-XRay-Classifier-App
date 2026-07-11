import streamlit as st
import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

st.set_page_config(page_title="Chest X-Ray Classifier", page_icon="🫁")

st.title("🫁 Chest X-Ray Pathology Classifier")
st.write("Upload a frontal chest X-ray to detect 14 thoracic diseases.")
st.write("Built by Tisha Chatterjee | Independent Researcher")

# Load model architecture first (DenseNet-121)
@st.cache_resource
def load_model():
    # Create the model architecture
    model = models.densenet121(weights=None)  # No pretrained weights, we'll load yours
    
    # Replace classifier for 14 classes (same as your training)
    num_features = model.classifier.in_features
    model.classifier = nn.Linear(num_features, 14)
    
    # Load YOUR trained weights
    model.load_state_dict(torch.load('best_model.pth', map_location='cpu'))
    model.eval()
    return model

model = load_model()

# Same preprocessing as your training
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

CLASSES = ['Atelectasis', 'Cardiomegaly', 'Consolidation', 'Edema', 
           'Effusion', 'Emphysema', 'Fibrosis', 'Hernia', 'Infiltration',
           'Mass', 'Nodule', 'Pleural Thickening', 'Pneumonia', 'Pneumothorax']

uploaded_file = st.file_uploader("Choose a chest X-ray image (PNG or JPG)", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(image, caption='Uploaded X-Ray', use_column_width=True)
    
    with col2:
        st.subheader("Predicted Probabilities")
        img = transform(image).unsqueeze(0)
        with torch.no_grad():
            outputs = model(img)
            probs = torch.sigmoid(outputs).squeeze().tolist()
        
        for i in range(len(CLASSES)):
            prob = round(probs[i] * 100, 1)
            st.write(f"**{CLASSES[i]}:** {prob}%")
            st.progress(prob / 100)