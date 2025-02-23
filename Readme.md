# Convert PDF to HTML

### Build the container
```bash
docker build -t pdf2html .
```

### Run the container
```bash
docker run pdf2html:latest
```

### Check if service is running
```bash
curl http://<your_local_ip>:5000
```
The output should be
```bash
Flask server is running!
```

### Converting the PDF to HTML
```bash
curl -X POST -F "pdf=@<path/to/pdf/file.pdf>" http://<your_local_ip>:5000/convert
```
The output should be
```bash
{"message":"Conversion successful","output":"/tmp/<your_file.pdf.html>"}
```
The HTML file and its images are saved on the container /tmp folder