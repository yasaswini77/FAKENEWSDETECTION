import pandas as pd

# Sample dataset with a categorical feature (Source)
data = pd.DataFrame({'Source': ['Social Media', 'News Website', 'Blog', 'Social Media', 'Blog']})

# One-hot encoding
one_hot_encoded = pd.get_dummies(data['Source'], prefix='Source')
print("One-Hot Encoding:")
print(one_hot_encoded)

# Label encoding
label_encoded = data['Source'].astype('category').cat.codes
print("\nLabel Encoding:")
print(label_encoded)
