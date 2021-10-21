import xml.etree.cElementTree as et

root = et.Element("Edificio_2")

se = et.SubElement(root,"Entornos")
et.SubElement(se,"Alumno").text = "Cristian Alejandro Hernandez Dominguez"
et.SubElement(se,"Matricula").text = "18040015"

et.SubElement(se,"Alumno").text = "Luis Alberto Rangel Mireles"
et.SubElement(se,"Matricula").text = "18040024"

et.SubElement(se,"Alumno").text = "Coral Jocelyn Salamanca Muños"
et.SubElement(se,"Matricula").text = "18040036"

et.SubElement(se,"Alumno").text = "Sayra Xiomara Ibarra Casas"
et.SubElement(se,"Matricula").text = "18040010"

et.SubElement(se,"Alumno").text = "Ana Carolina Malacara Berlanga"
et.SubElement(se,"Matricula").text = "18040016"

se = et.SubElement(root,"Redes_Inteligentes")
et.SubElement(se,"Alumno").text = "Andrea Guadalupe Rojas Lopez"
et.SubElement(se,"Matricula").text = "18040089"

et.SubElement(se,"Alumno").text = "Nadia Itzel Villanueva Cortez"
et.SubElement(se,"Matricula").text = "18010904"

et.SubElement(se,"Alumno").text = "Xochitl Anahi Ovalle Macias"
et.SubElement(se,"Matricula").text = "18040078"

et.SubElement(se,"Alumno").text = "Luis Angel Sanchez Ortiz"
et.SubElement(se,"Matricula").text = "18040093"

et.SubElement(se,"Alumno").text = "Gerardo Amador Rojas Lopez"
et.SubElement(se,"Matricula").text = "18040018"

se = et.SubElement(root,"Desarrollo_de_Software")
et.SubElement(se,"Alumno").text = "Andrea Guadalupe Rojas Lopez"
et.SubElement(se,"Matricula").text = "18040089"

et.SubElement(se,"Alumno").text = "Nadia Itzel Villanueva Cortez"
et.SubElement(se,"Matricula").text = "18010904"

et.SubElement(se,"Alumno").text = "Xochitl Anahi Ovalle Macias"
et.SubElement(se,"Matricula").text = "18040078"

et.SubElement(se,"Alumno").text = "Luis Angel Sanchez Ortiz"
et.SubElement(se,"Matricula").text = "18040093"

et.SubElement(se,"Alumno").text = "Gerardo Amador Rojas Lopez"
et.SubElement(se,"Matricula").text = "18040018"

tree = et.ElementTree(root)
tree.write("Edificio_2.xml", xml_declaration=True)
