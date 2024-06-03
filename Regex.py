# Q1 Task 1

import re

text = "Contact emails are: john.doe@example.com and jane.doe@example.com."

# Corrected Regular Expression
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

print(emails)

# Q2 Task 1

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
exclude_domain = "exclude.com"

# Negative Lookahead Assertion
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(?!%s)\b" % exclude_domain, text)
print(emails)

# Q1 Task 1

import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
key_to_extract = "Occupation"

# Positive Lookbehind Assertion
pattern = r"(?<=%s: )([^;]+)" % key_to_extract
match = re.search(pattern, text)

if match:
  extracted_value = match.group(1)
  print(f"Extracted value for '{key_to_extract}': {extracted_value}")
else:
  print(f"Key '{key_to_extract}' not found in the text.")

# Q 3 Task 1

import re

def extract_value(text, key_to_extract):
  """Extracts the value corresponding to a specific key from formatted text.

  Args:
      text: The formatted text containing data entries (str).
      key_to_extract: The specific key to extract the value for (str).

  Returns:
      The extracted value (str) or None if the key is not found.
  """

  pattern = r"(?<=%s: )([^;]+)" % re.escape(key_to_extract)  # Escape special characters
  match = re.search(pattern, text)

  if match:
    return match.group(1)
  else:
    return None

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
key_to_extract = "Occupation"

extracted_value = extract_value(text, key_to_extract)

if extracted_value:
  print(f"Extracted value for '{key_to_extract}': {extracted_value}")
else:
  print(f"Key '{key_to_extract}' not found in the text.")

# Q4 Task 1

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set",
    "High-definition TV with a sleek design (Price: $499.99)"  # Added an example with price
]

keywords = {
    "electronics": ["smartphone", "tv", "screen", "memory"],
    "apparel": ["t-shirt", "shirt", "clothing"],
    "home_and_kitchen": ["knife", "kitchen", "stainless steel"]
}

def tag_product(description):
  """Tags a product based on keyword matches in its description.

  Args:
      description: The product description (str).

  Returns:
      A list of tags associated with the product (list of str).
  """

  tags = []
  for category, keywords_list in keywords.items():
    for keyword in keywords_list:
      if re.search(rf"\b{keyword}\b", description, flags=re.IGNORECASE):  # Case-insensitive search
        tags.append(category)
        break  # Stop searching keywords once a match is found for a category

  return tags

for description in descriptions:
  product_tags = tag_product(description)
  if product_tags:
    print(f"Product Description: {description}")
    print(f"Tags: {', '.join(product_tags)}")
  else:
    print(f"Product Description: {description}")
    print("No tags found.")
  print()


