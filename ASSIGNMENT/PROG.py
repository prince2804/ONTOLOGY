import xml.etree.ElementTree as ET
from rdflib import Graph, Namespace, Literal, URIRef
from owlready2 import get_ontology

# Load the OWL ontology
ontology_file = "CS22M066.rdf"

# 1. Parse the XML file
tree = ET.parse('assignment1.xml')
root = tree.getroot()

# 2. Define the ontology namespace
ns = Namespace("http://example.org/ontology#")

# 3. Extract XML data and convert to RDF triples
graph = Graph()
for user_elem in root.findall('.//user'):
    user_id = user_elem.get('id')
    username = user_elem.get('username')
    email = user_elem.get('email')
    # Extract other relevant user attributes
    
    # Create user resource and add attributes as RDF triples
    user_uri = URIRef(f"http://example.org/users/{user_id}")
    graph.add((user_uri, ns.username, Literal(username)))
    graph.add((user_uri, ns.email, Literal(email)))
    # Add other user attributes as RDF triples
    
    # Extract profile data and add as RDF triples
    profile_elem = user_elem.find('profile')
    if profile_elem is not None:
        # Extract profile attributes and add as RDF triples
        location = profile_elem.get('location')
        education = profile_elem.get('education')
        occupation = profile_elem.get('occupation')
        # Add profile attributes as RDF triples
        graph.add((user_uri, ns.location, Literal(location)))
        graph.add((user_uri, ns.education, Literal(education)))
        graph.add((user_uri, ns.occupation, Literal(occupation)))
    
    # Extract post data and add as RDF triples
    for post_elem in user_elem.findall('posts/post'):
        post_id = post_elem.get('id')
        timestamp = post_elem.get('timestamp')
        # Extract other relevant post attributes
        
        # Create post resource and add attributes as RDF triples
        post_uri = URIRef(f"http://example.org/posts/{post_id}")
        graph.add((post_uri, ns.timestamp, Literal(timestamp)))
        # Add other post attributes as RDF triples
        
        # Connect user and post with appropriate RDF triples
        graph.add((user_uri, ns.posts, post_uri))

# 5. Combine RDF triples with the ontology

# Optionally, serialize the RDF graph
graph.serialize(destination='output.rdf', format='xml')