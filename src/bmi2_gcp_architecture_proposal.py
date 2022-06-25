from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.compute import Run
from diagrams.gcp.network import LoadBalancing, Armor, CDN, DNS
from diagrams.gcp.storage import Storage
from diagrams.gcp.database import SQL
from diagrams.generic.device import Mobile, Tablet
from diagrams.onprem.client import Client

with Diagram("BMI2 GCP Architecture Proposal", filename="../diagrams/bmi2_gcp_architecture_proposal"):
    with Cluster("clients"):
        clients = [ Mobile("mobile"), Client("browser") ]

    dns = DNS("Cloud DNS")

    cdn = CDN("Cloud CDN")

    glb = LoadBalancing("Global Load Balancer")

    app_armor = Armor("Cloud Armor")

    with Cluster("Frontend Services"):
        with Cluster("Cloud Run"):
            with Cluster("Web Servers"):
                web_servers = Run("web")

        storage = Storage("Static File Storage")

    ilb = LoadBalancing("Internal Load Balancer")

    with Cluster("Backend Services"):
        with Cluster("Cloud Run"):
            with Cluster("Application Servers"):
                app_servers = Run("app")

        db = SQL("Cloud SQL")

    clients >> dns
    clients >> cdn
    cdn >> glb
    glb >> Edge(label="DDoS Protection and WAF") >> app_armor
    glb >> web_servers
    web_servers >> storage
    web_servers >> ilb
    ilb >> app_servers
    app_servers >> db
