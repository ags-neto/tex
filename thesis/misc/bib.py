import re

def extract_titles_from_bib(bib_file, output_txt):
    """
    Extracts all titles from a .bib file and writes them to a .txt file.

    Parameters:
        bib_file (str): Path to the .bib file.
        output_txt (str): Path to the output .txt file.
    """
    try:
        with open(bib_file, 'r', encoding='utf-8') as file:
            bib_content = file.read()

        # Regular expression to match titles
        titles = re.findall(r"title\s*=\s*\{([^}]+)\}", bib_content)

        # Write the titles to the output file
        with open(output_txt, 'w', encoding='utf-8') as output_file:
            for title in titles:
                output_file.write(title.strip() + "\n")

        print(f"Extracted {len(titles)} titles and wrote them to {output_txt}.")

    except FileNotFoundError:
        print(f"Error: The file {bib_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_bib = "thesis/bibliography/references.bib"  # Replace with your .bib file path
    output_txt = "thesis/bibliography/titles.txt"  # Replace with your desired .txt file path
    extract_titles_from_bib(input_bib, output_txt)
