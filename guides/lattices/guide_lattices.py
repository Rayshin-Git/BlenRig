from os.path import dirname, join
from .. lattices.guide_lattices_actions import *

images_dir = join(dirname(__file__), 'images')

GUIDE_STEPS_LATTICES = (
    #Introduction
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Introduction',
            'ES': 'Introducción'
            },
        'texto': {
            'EN': "In this Guide you will adjust the placement of the Lattices of the rig. Lattices will allow you to achieve extra deformations, most commonly used for toon characters.",
            'ES': "En esta Guia, tu podras ajustar el posicionamiento del Lattices del rig. El Lattices te permitira lograr una deformaciones adicionales,más comúnmente utilizadas para los personajes toon."
            },
        'accion': LATTICES_Intro
    },
    #Edit Body Lattice
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Edit Body Lattice',
            'ES': 'Edita el Lattice del cuerpo'
            },
        'texto': {
            'EN': "Adjust the Body Lattice, press the 'Edit Lattice Position' to move the lattice, then press the 'Apply Lattice Position' button.",
            'ES': "Ajuste el Lattice del cuerpo, pulsa el botón 'Edit Lattice Position' para mover el lattice, luego pulse el botón 'Apply Lattice Position'."
            },
        'accion': LATTICES_Adjust_Body
    },
    #Edit Head Lattice
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Edit Head Lattice',
            'ES': 'Edita el Lattice de la cabeza'
            },
        'texto': {
            'EN': "Adjust the Head Lattice, press the 'Edit Lattice Position' to move the lattice, then press the 'Apply Lattice Position' button.",
            'ES': "Ajusta el Lattice de la cabeza, pulsa el botón 'Edit Lattice Position' para mover el lattice, luego pulse el botón 'Apply Lattice Position'."
            },
        'accion': LATTICES_Adjust_Head
    },
    #Edit Brow Lattice
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Edit Brow Lattice',
            'ES': 'Edita el Lattice de las cejas'
            },
        'texto': {
            'EN': "Adjust the Brow Lattice, press the 'Edit Lattice Position' to move the lattice, then press the 'Apply Lattice Position' button.",
            'ES': "Ajusta el Lattice de las cejas, pulsa el botón 'Edit Lattice Position' para mover el lattice, luego pulse el botón 'Apply Lattice Position'."
            },
        'accion': LATTICES_Adjust_Brow
    },
    #Edit Mouth Lattice
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Edit Mouth Lattice',
            'ES': 'Edita el Lattice de la boca'
            },
        'texto': {
            'EN': "Adjust the Mouth Lattice, press the 'Edit Lattice Position' to move the lattice, then press the 'Apply Lattice Position' button.",
            'ES': "Ajusta el Lattice de la boca, pulsa el botón 'Edit Lattice Position' para mover el lattice, luego pulse el botón 'Apply Lattice Position'."
            },
        'accion': LATTICES_Adjust_Mouth
    },
    #Edit Eyes Lattice
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Edit Eyes Lattices',
            'ES': 'Edita el Lattice de los ojos'
            },
        'texto': {
            'EN': "Adjust the Lattice of the Left Eye, press the 'Edit Lattice Position' to move the lattice, then press the 'Apply Lattice Position' button. Finally Mirror the position to the Right Eye Lattice with the 'Mirror Lattice Transforms' button",
            'ES': "Edita el Lattice de los ojos, pulsa el botón 'Edit Lattice Position' para mover el lattice, luego pulse el botón 'Apply Lattice Position'."
            },
        'accion': LATTICES_Adjust_Eyes
    },
    #Lattices Finish
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Lattices Finish',
            'ES': 'Edita el Lattice del cuerpo'
            },
        'texto': {
            'EN': "Done! Move to the Weight Painting Guide!",
            'ES': "Ajuste el Lattice del cuerpo, pulsa el botón 'Edit Lattice Position' para mover el lattice, luego pulse el botón 'Apply Lattice Position'."
            },
        'accion': LATTICES_Finish
    }
)



