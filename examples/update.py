from lib4vex.parser import VEXParser
from lib4vex.generator import VEXGenerator
from lib4sbom.data.vulnerability import Vulnerability
from lib4vex.data.product import VEXProduct
from lib4vex.data.metadata import VEXMetadata
import sys

vextype=sys.argv[2]

vexparser = VEXParser(vex_type=vextype)
# Read VEX file
vexparser.parse(sys.argv[1])

# Extract key elements of VEX document
#metadata=vexparser.get_metadata()
#print (metadata)
vexmetadata=VEXMetadata()
vexmetadata.set_metadata(vexparser.get_metadata())
# Product information
product=vexparser.get_product()
print ("PRODUCT=============")
for key in product:
    #print (key)
    #print (product[key])
    vexproduct = VEXProduct()
    vexproduct.set_product(key,product[key])
    print (f"VEX document for {vexproduct.get_name()} release {vexproduct.get_release()} produced on {vexmetadata.get_date()}")
    #print (vexproduct.get_release())

# Reported vulnerabilities
print ("VULN==========")
vulnerabilities=vexparser.get_vulnerabilities()
for v in vulnerabilities:
    #print(v)
    print ("ID", v.get("id"))
    print ("Last update", v.get('created'))
    print ("Description", v.get("description"))
    print ("Status", v.get("status"))
    print ("Justification", v.get("justification"))










