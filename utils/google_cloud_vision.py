# utils/google_cloud_vision.py
from google.cloud import vision

EMPTY_ARGS = 'Api google.cloud.vision needs uri or content and none provided.'


def get_best_guess(uri=None, content=None, max_results=10):
    """
    Get top results from the best guess using google vision apis.
    TODO force structure to this function
    :param uri: public uri of the image
    :param content: image binary content
    :param max_results: maximum number of results to be returned
    :return: top results
    """
    client = vision.ImageAnnotatorClient()

    if uri is None and content is None:
        # throw error for invalid arguements
        raise ValueError(EMPTY_ARGS)

    if content is None:
        image = vision.types.Image()
        image.source.image_uri = uri
    else:
        image = vision.types.Image(content=content)

    response = client.web_detection(image=image)
    annotations = response.web_detection

    recipe_names = []
    if annotations.web_entities:
        print('%d Web entities found.' % len(annotations.web_entities))

        for entity in list(annotations.web_entities)[:max_results]:
            recipe_names.append({'name': entity.description})
    else:
        print('0 Web entities found.')

    return recipe_names
