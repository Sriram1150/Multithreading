import threading
import requests
import time
import os

def fetch_and_save(link, directory="downloads"):
    output_file = os.path.join(directory, link.split("/")[-1])
    try:
        data = requests.get(link)
        with open(output_file, "wb") as file:
            file.write(data.content)
        print(f"Downloaded: {output_file}")
    except Exception as error:
        print(f"Failed to download {link}: {error}")

def run_sequential(links):
    for link in links:
        fetch_and_save(link)

def run_parallel(links):
    workers = []
    for link in links:
        worker = threading.Thread(target=fetch_and_save, args=(link,))
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()

def get_links_from_file(path):
    with open(path, "r") as file:
        return [line.strip() for line in file if line.strip()]

if __name__ == "__main__":
    os.makedirs("downloads", exist_ok=True)

    mode = input("Enter 1 to input URLs manually, 2 to read from file: ")

    if mode == "1":
        links = input("Enter URLs separated by spaces:\n").split()
    else:
        file_name = input("Enter filename (e.g., urls.txt): ")
        links = get_links_from_file(file_name)

    print("\nSequential Downloading...")
    start_time = time.time()
    run_sequential(links)
    end_time = time.time()
    print(f"Sequential download time: {end_time - start_time:.2f} seconds")

    print("\nConcurrent Downloading...")
    start_time = time.time()
    run_parallel(links)
    end_time = time.time()
    print(f"Concurrent download time: {end_time - start_time:.2f} seconds")