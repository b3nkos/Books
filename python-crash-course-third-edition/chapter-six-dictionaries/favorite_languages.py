favorite_languages = {
    "jose": "python",
    "maria": "java",
    "luis": "javascript",
    "ana": "python"
}

print("Names:")
for name in favorite_languages.keys():
    print(name.title())

print("\nLanguages:")
for language in set(favorite_languages.values()):
    print(language.lower())