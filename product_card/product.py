from fasthtml.common import *
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    image: str
    description: str
    specs: List[str]

pipe = Product(
    name='Stainless steel seamless tube',
    price=10.00,
    image='product_card/assets/pipe.png',
    description='High-quality 347 stainless steel pipe, seamless construction for maximum durability. This premium product is designed to meet the highest industry standards and is suitable for a wide range of applications in various sectors.',
    specs=['DN200, OD 219.1 mm x 18 mm wall',
            '110 cm standard length (cut to your specifications)',
            'Excellent pressure resistance',
            'Versatile for various industrial and construction applications',
            'Corrosion-resistant properties',
            'High temperature tolerance']
)

app = FastHTML()

# For images, CSS, etc.
@app.get("/{fname:path}.{ext:static}")
def static(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')

@app.route("/")
def get():
    return Html(
    Head(Title("Product Card"), Link(rel='stylesheet', href='product_card/assets/style.css', type='text/css')),
    Body(
    Div(cls='product-card')(
        Img(src=pipe.image, alt=pipe.name, cls='product-image'),
        Div(cls='product-info')(
            H2(pipe.name, cls='product-title'),
            Div(cls='button-group')(
                Button(cls='button')(
                    'Add to shopping cart'
                ),
                Button(cls='button')(
                    'Add to list'
                )
            ),
            P(pipe.description, cls='product-description'),
            Ul(cls='product-specs')(
                (Li(spec) for spec in pipe.specs)
                # Li('DN200, OD 219.1 mm x 18 mm wall'),
                # Li('110 cm standard length (cut to your specifications)'),
                # Li('Excellent pressure resistance'),
                # Li('Versatile for various industrial and construction applications')
            ),
            Button('Search for similar items', cls='search-button')
        )
    )
)
)

serve()