import requests
import re

# Define your GitHub repository URL
repository_url = "https://api.github.com/repos/bujo-eayn/pooii/contributors"

# Fetch contributors data from GitHub API
response = requests.get(repository_url)
contributors = response.json()

# Create a list of contributor profiles with avatars and names
contributor_list = []
for contributor in contributors:
    contributor_avatar_url = contributor["avatar_url"]
    contributor_name = contributor["login"]
    contributor_profile = f"[![{contributor_name}]({contributor_avatar_url}&s=60)](https://github.com/{contributor_name})"
    contributor_list.append(contributor_profile)

# Read the CONTRIBUTORS.md file
with open("CONTRIBUTORS.md", "r") as file:
    content = file.read()

# Replace the CONTRIBUTORS-LIST section in CONTRIBUTORS.md with the updated list
content = re.sub(r"<!-- CONTRIBUTORS-LIST:START -->(.|\n)*<!-- CONTRIBUTORS-LIST:END -->",
                 "<!-- CONTRIBUTORS-LIST:START -->\n" + "\n".join(contributor_list) + "\n<!-- CONTRIBUTORS-LIST:END -->",
                 content)

# Write the updated content back to CONTRIBUTORS.md
with open("CONTRIBUTORS.md", "w") as file:
    file.write(content)
