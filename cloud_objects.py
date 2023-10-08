import bpy
import csv

def is_number_tryexcept(s):
    """ Returns True if string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False

def create_sphere(x, y, z):
    print(f"{x},{y},{z}")
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(float(x), float(y), float(z)))
    sphere = bpy.context.object
    sphere.data.materials.append(material)


# Create the material (white)
#material = bpy.data.materials.new(name="White")
#material.use_nodes = True
#material.node_tree.nodes.clear()

#bsdf_node = material.node_tree.nodes.new(type="ShaderNodeBsdfPrincipled")
#bsdf_node.inputs['Base Color'].default_value = (1, 1, 1, 1)

#output_node = material.node_tree.nodes.new(type="ShaderNodeOutputMaterial")
#material.node_tree.links.new(bsdf_node.outputs['BSDF'], output_node.inputs['Surface'])


with open("C:\\Users\\densh\\PycharmProjects\\starchart\\objects.csv", 'r') as file:
    # Create a CSV reader
    reader = csv.reader(file)
    skip = True
    for row in reader:
        if skip:
            skip = False
            continue
        x,y,z = row
        create_sphere(x,y,z)
