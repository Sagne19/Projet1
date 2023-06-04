import streamlit as st

# Ajouter des onglets à l'application
tabs = st.tabs(["Page 1", "Page 2", "Page 3","Page 4","Page 5","Page 6","Page 7"])

# Contenu de la première page
with tabs[0]:
    st.markdown("<h1 style='text-align: center;'>Bienvenue sur l'application CrossWay !</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>L'application qui soigne vos plaies !</h3>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("<style>div.stButton > button:first-child {margin-left: auto;margin-right: auto;display: block;}</style>", unsafe_allow_html=True)
    st.button('Commencez ici 👈🏼')

# Contenu de la deuxième page

with tabs[1]:
    st.title("Veuillez sélectionner votre typologie de plaie ")

# Définir les options de sélection
    options = ['Escarres', 'Plaies Chirurgicales', 'Autre(s) types(s) de plaie', "Voies D'abord"]

    # Afficher la sélection sur Streamlit
    selected_option = st.multiselect('Choisissez parmi la liste ci-dessous : ', options)


    # Afficher le résultat sélectionné
    st.write('Vous avez sélectionné :', ", ".join(selected_option))
    st.button('Étape suivante')

with tabs[2] :
    
    st.markdown(
        """
        <style>
        .box {
            border: 1px white black;
            padding: 10px;
            border-radius: 5px;
            background-color: #f2f2f2;
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Affichage du contenu encadré dans la boîte avec fond gris clair
    st.markdown(
        """
        <div class="box">
            <p>Définition :</p>
            <p>Une escarre est une lésion cutanée d'origine ischémique liée à une compression des tissus mous entre un plan dur et les saillies osseuses</p>
        </div>
        """,
        unsafe_allow_html=True
    )


    # Utilisation de la fonction st.markdown pour appliquer un style CSS personnalisé
    st.markdown(
        """
        <style>
        .custom-checkbox {
            background-color: #555555;
            padding: 10px;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Création des colonnes
    st.write('Stade Escarre')
    col12, col13, col14 = st.columns(3)

    # Ajout du fond gris foncé aux checkboxes
    entree_1 = col12.checkbox("Stade 2")
    entree_2 = col13.checkbox("Stade 3")
    entree_3 = col14.checkbox("Stade 4")

    st.markdown("<br><br>", unsafe_allow_html=True)
    

    st.button("Je valide ")


with tabs[3]:
    st.title("🔎 Localisation de l'escarre")

    # Création des colonnes
    col1, col2 = st.columns(2)

    # Checkbox dans la première colonne
    entree_1 = col1.checkbox("Talon Droit")
    entree_2 = col1.checkbox("Talon Gauche")
    entree_3 = col1.checkbox("Malléole Droite")
    entree_4 = col1.checkbox("Malléole Gauche")

    # Checkbox dans la deuxième colonne
    entree_5 = col2.checkbox("Sacrum")
    entree_6 = col2.checkbox("Trochanter Droit")
    entree_7 = col2.checkbox("Trochanter Gauche")
    entree_8 = col2.checkbox("Autres")


    # Bouton "Je valide"
    if any([entree_1, entree_2, entree_3, entree_4, entree_5, entree_6, entree_7, entree_8]) and st.button("Je valide"):
        # Sélection de la localisation
        selected_items = []
        if entree_1:
            selected_items.append("Talon Droit")
        if entree_2:
            selected_items.append("Talon Gauche")
        if entree_3:
            selected_items.append("Malléole Droite")
        if entree_4:
            selected_items.append("Malléole Gauche")
        if entree_5:
            selected_items.append("Sacrum")
        if entree_6:
            selected_items.append("Trochanter Droit")
        if entree_7:
            selected_items.append("Trochanter Gauche")
        if entree_8:
            selected_items.append("Autres")

        if selected_items:
            selection = st.write("Vous avez sélectionné :", ", ".join(selected_items))
            
        else:
            st.write("Aucune option sélectionnée.")


# Contenu de la troisième page
with tabs[4]:
    
    st.title("Renseignements complémentaires")

    with st.form("Formulaire"):
        st.write('Merci de renseigner les champs ci-dessous : ')

        # Champs de saisie
        dimensions = st.text_input("Dimensions de l'escarre : ")
        profondeur = st.text_input("Profondeur de l'escarre : ")
        quantite_exsudat = st.radio("Quantité de l'exsudat", ("Absence", "Abondant", "Peu"))
        decollement = st.radio("Décollement", ("Oui", "Non"))
        quantite_peau_perilesionnelle = st.radio("Quantité de la peau périlésionnelle", ("Macération", "Sèche","Inflammatoire"))
        moderation_berges = st.radio("Macération des berges", ("Oui", "Non"))
        douleur = st.radio("Douleur", ("Oui", "Non"))
        phlyctene = st.radio("Phlyctène", ("Oui", "Excision"))

        # Bouton de soumission
        submitted = st.form_submit_button('Soumettre')

        if submitted:
            st.write("Votre formulaire a bien été envoyé!")


    
with tabs[5]:
    st.title("Soins réalisés")
    col15, col16 = st.columns(2)
    with col15:

        st.markdown(
            """
            <style>
            .box-col15 {
                border: 1px solid black;
                padding: 10px;
                border-radius: 5px;
                background-color: #ADD8E6; /* Bleu clair */
                color: black;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="box-col15" style="text-align: center;">
                <p>Prescription médicale du protocole de soin 📑</p>
                <button style="padding: 10px 20px;">Je télécharge</button>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.markdown(
            """
            <div class="box-col15">
                <p><u>Objectif de la cicatrisation :</u></p>
                <label><input type="checkbox"> Détersion </label><br>
                <label><input type="checkbox"> Bourgeonnement</label><br>
                <label><input type="checkbox"> Épithélialisation</label><br>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.markdown(
            """
            <div class="box-col15" style="text-align: center;">
                <p>Photos prises de la plaie lors de la réfection du pansement 📸</p>
                <button style="padding: 10px 20px;">Je télécharge</button>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.markdown(
            """
            <div class="box-col15" style="text-align: center;">
                <br>
                <p>Dimensions et références des pansements utilisés 🩹 </p>
                <br>
                <label><input type="input"></label>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with col16:
        st.markdown(
            """
            <style>
            .box-col16 {
                border: 1px solid black;
                padding: 10px;
                border-radius: 5px;
                background-color: #E6E6FA; /* Violet clair */
                color: black;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="box-col16">
            <p><u>Lit de la plaie :</u></p>
                <label><input type="checkbox"> Nettoyage</label><br>
                <label><input type="checkbox"> Désinfection</label><br>
                <label><input type="checkbox"> Détersion mécanique</label><br>
                <br>
            <p><u>Pansement primaire :</u></p>
                <label><input type="checkbox"> Interface</label>
                <label><input type="checkbox"> Hydrogel</label>
                <label><input type="checkbox"> Alginate</label>
                <label><input type="checkbox"> Miel</label>
                <label><input type="checkbox"> Hydrocellulaire</label>
                <label><input type="checkbox"> Hydrofibre</label>
                <label><input type="checkbox"> Irrigo-absorbant absorbant</label>
                <label><input type="checkbox"> TPN</label>
                <label><input type="checkbox"> Hydrocolloide</label>
                <label><input type="checkbox"> Acide Hyaluronique</label>
                <br>
                <br>
            <p><u>Pansement secondaire :</u></p>
                <label><input type="checkbox"> Compresses stériles</label>
                <label><input type="checkbox"> Tampon absorbant américain</label><br>
                <label><input type="checkbox"> Bandes</label>
                <label><input type="checkbox"> Pansements stériles avec compresses</label>
                <label><input type="checkbox"> Film de polyuréthane</label>
                <br>
                <br>
            <p><u>Peau périlésionnelle :</u></p>
                <label><input type="checkbox"> Acide Hyaluronique</label>
                <label><input type="checkbox"> Dermocorticoïde</label>
                <label><input type="checkbox"> Ablation de l'hyperKératose</label>
                <br>
                <br>
            <p>Commentaire(s) :</p>
            <textarea></textarea>
            <br>
            <br>
            </div>
            """,
            unsafe_allow_html=True
        )

    ## Ajout d'un espace
    st.markdown("<br><br>", unsafe_allow_html=True)
    # Créez un bouton "Valider"
    if st.button("Valider"):
        # Affichez le message de réussite
        st.success("Votre fiche a bien été complétée")




# Contenu de la sixième page
with tabs[6]:
    st.title("Date du soin et du protocole")

    # Checkbox dans la première colonne
    date_value_1 = st.date_input("Date du soin")
    st.write("Soin réalisé le :", date_value_1, "par SCLAFER Emeline (IDE)")

    # Checkbox dans la deuxième colonne
    date_value_2 = st.date_input("Date du protocole")
    st.write("Protocole de soin réalisé le :", date_value_2, "par BARBOU Justine (Médecin)")

    
