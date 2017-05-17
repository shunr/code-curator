# Code Curator

Python utility to generate an archive from code you've written on competitive programming platforms and organize them nicely. Here's an [example](https://github.com/shunr/competitive-programming) of what is generated.

## Supported platforms
- DMOJ

## Installation
Clone this repo
```shell
git clone https://github.com/shunr/code-curator.git
cd code-curator
```
Install dependencies
```shell
pip install -r requirements.txt
```
Create configuration file
```shell
cp config.example.json config.json
```
### Usage
```shell
python3 curate.py
```

## Configuration
| Option | Description |
|---|---|
|```platforms```| Contains configuration for authentication on different platforms, one object with ```username``` and ```password``` keys for each platform |
|```output_path```| Relative or absolute path to generate the repository |
|```readme_name```| Filename of automatically generated table of contents (keep as ```REAME.md``` for GitHub) |
|```readme_title```| Title that will be displayed in the header of the table of contents |
|```readme_description```| Markdown description that will appear in the generated header |

### Sample configuration
```json
{
  "platforms": {
    "dmoj": {
      "username": "wew_lad",
      "password": "correcthorsebatterystaple"
    }
  },
  "output_path": "output",
  "readme_name": "README.md",
  "readme_title": "Competitive Programming Archive",
  "readme_description": "Curated automagically using [Code Curator](https://github.com/shunr/code-curator)"
}
```