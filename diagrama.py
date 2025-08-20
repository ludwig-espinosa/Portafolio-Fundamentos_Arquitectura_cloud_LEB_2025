from graphviz import Digraph

# Crear diagrama de arquitectura
dot = Digraph("ArquitecturaMediaStream", format="png")

# Estilo general
dot.attr(bgcolor="white")
dot.attr("node", shape="box", style="rounded,filled", color="lightblue", fontname="Arial")

# Nodos principales
dot.node("Users", "Usuarios Globales\n(Web/App)", shape="oval", color="lightgreen")
dot.node("CF", "Amazon CloudFront\n(CDN)", color="orange")
dot.node("S3", "Amazon S3\n(Almacenamiento de Objetos)", color="lightblue")
dot.node("Glacier", "Amazon S3 Glacier\n(Archivado)", color="lightgrey")
dot.node("IAM", "AWS IAM\n(Control de Acceso)", color="yellow")
dot.node("KMS", "AWS KMS\n(Cifrado)", color="pink")

# Relaciones
dot.edge("Users", "CF", label="Solicitudes de contenido")
dot.edge("CF", "S3", label="Distribución optimizada")
dot.edge("S3", "Glacier", label="Archivado automático")
dot.edge("IAM", "S3", label="Políticas de acceso")
dot.edge("KMS", "S3", label="Cifrado de objetos")

# Renderizar el archivo
output_path = "/mnt/data/arquitectura_mediastream"
dot.render(output_path, cleanup=True)

output_path + ".png"
