# django-rest-api

## set up 

```
pip install -r requirements.txt
```

# backend
- django backend

# pyclient
- consumes the backend

## creating client 

rest api is for software to communicate with each other over the web  


## Get random thing from db

```
Product.objects.all().order_by("?").first()
```

## serialisation:

model serialisers
- tools that help convert complex data types (e.g. Django models) into formats that can be easily rendered into JSON, XML, or other content types
- also handle the reverse process: validating / deserializing input data back into complex types e.g. model instances

serializer helps change model representation for any given view
meta class: makes it clear which model the serializer is based on, what fields to include, and any other specific behaviors you want to enforce

Serialization: 
    - taking a Django model instance (e.g. a row in a database table) 
    - turning it into a JSON object that can be sent over the internet
    - allows data to be easily shared / read by other systems

Deserialization: 
    - taking data from a JSON object (received from a web request)
    - turning it back into a Django model instance
    - useful when receiving data from a user, validating it, and saving it to your database.

## class based views (CBVs)

- way to define views instead of functions
- each class represents a view & can contain methods that define behaviour for different HTTP methods
- encapsulates logic in a more organised / reusable way

- can organise code better by separating functionality into methods (get, put, post, delete)
- by inheriting from base classes, you can reuse code
    - reduces redundancy / makes it easier to maintain
- can create custom views by extending django's built in views
    - easier to add / override functionality without starting from scratch

## generic views

- prebuilt views to handle common tasks
- built on top of CBVs
- save time by handling common patterns

- efficiency: use views with minimal configuration
- consistency: consistent structure and behaviour = code easier to read / understand
- flexible

## function based views vs class based views

this:

```
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialiser

    # method for overriding object save / deletion behaviour
    def perform_create(self, serializer):

        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        # if user doesnt provide content for new object, set it to be the title
        if content is None:
            content = title

        serializer.save(content=content)

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    # has to be serializer not serialiser!!!
    serializer_class = ProductSerialiser
```

does the same thing as this:

```
@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        # if theres a pk, its one object, you want to see its details
        if pk is not None:
            product = get_object_or_404(Product, pk=pk)
            data = ProductSerialiser(product).data
            return Response(data)
        # if theres no pk, its multiple object, list them
        queryset = Product.objects.all()
        data = ProductSerialiser(queryset, many=True).data # serializing multiple objects
        return Response(data)
    
    if method == 'POST':
        serializer = ProductSerialiser(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            # if user doesnt provide content for new object, set it to be the title
            if content is None:
                content = title
                serializer.save(content=content)
        return Response({"invalid": "data"}, status=400)
```

but the first one is cleaner and can be replicated easier. if someone else comes along they dont need to read through and understand your code. 

