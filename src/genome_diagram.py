# This script generates a Genome Diagram for the plasmids
# Part of the COVID-19.Tracker project
from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram

from Bio import SeqIO

record = SeqIO.read("data/genome.gb", "genbank")

gd_feature_set = GenomeDiagram.FeatureSet()
for feature in record.features:
    if feature.type != "gene":
        continue
    if len(gd_feature_set) % 2 == 0:
        color = colors.blue
    else:
        color = colors.lightblue
    gd_feature_set.add_feature(feature, color=color, label=True)

gd_track_for_features = GenomeDiagram.Track(name="Annotated Features")
gd_diagram = GenomeDiagram.Diagram(
    "Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome")

gd_track_for_features.add_set(gd_feature_set)
gd_diagram.add_track(gd_track_for_features, 1)

gd_diagram.draw(format="circular", circular=True, pagesize=(20*cm, 20*cm),
                start=0, end=len(record), circle_core=0.7)
gd_diagram.write("data/plasmid_circular.png", "PNG")
Image("data/plasmid_circular.png")
