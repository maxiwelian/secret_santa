import google_images_download.google_images_download as dwn

response = dwn.googleimagesdownload()

arguments = {
    "keywords":"stone circle",
    "limit": 100,
    "print_urls":True,
    "related_images":True

}

paths = response.download(arguments)