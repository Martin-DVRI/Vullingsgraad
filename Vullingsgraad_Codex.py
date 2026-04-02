import streamlit as st
import math
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="K&L - Vullingsgraad",
    layout="wide"
)

# Dictionary met kokers en hun oppervlaktes
kokers = {
    'Koker 9,5x8,5': 8075.0,
    'Koker 11x15': 16500.0,
    'Koker 12x15': 15538.0,
    'Koker 13x32': 32472.0,
    'Koker 16x25': 40000.0,
    'Koker 25x42': 100500.0,
    'Koker 35x60': 207555.0,
    'Koker 45x60': 270000.0,
    'Max/2-H': 15500.0,
    'Max/3-H': 35650.0,
    'Buis 125 PP-HM': 7853.0,
    'Buis 170 PP-HM': 16741.0,
    'Buis 230 PP-HM': 31415.0,
    'Buis PE 110 SDR 17': 6361.0,
    'Buis PE 125 SDR 17': 9537.0,
    'Buis PE 160 SDR 17': 15614.0,
    'Buis PE 200 SDR 17': 24383.0,
    'Flexibele buis 90': 3870.0,
    'Flexibele buis 110': 5982.3,
    'Flexibele buis 125': 7793.1,
    'Flexibele buis 160': 13073.4,
    'Flexibele buis 200': 21895.2,
    'Buis GVB150': 17672.0,
    'Buis GVB200': 31416.0,
    'Kunststof klikbuis 58': 1964.0,
    'Kunststof klikbuis 83': 4418.0,
    'Kunststof klikbuis 110': 7854.0,
    'Kunststof klikbuis 160': 15615.0,
    'Buis PL110': 8333.0,
    'Buis PL125': 9435.0,
    'Buis PL163': 15394.0,
    'Buis PL 200': 21022.0,
    'Kunststof voering': 25480.0
}


# Dictionary met kabeltypes en hun diameters
kabels = {
    'SW 1,5kV': {
        'SW YMz1K 2x2,5': 14.4,
        'SW YMz1K 2x6': 16.6,
        'SW YMz1K 2x16': 21.1,
        'SW YMz1K 1x4x1,5': 15.5,
        'SW YMz1K 4x2,5': 15.8,
        'SW YMz1K 4x4': 16.4,
        'SW YMz1K 4x6': 17.6,
        'SW YMz1K 7x1,5': 16.5,
        'SW YMz1K 7x4': 18.6,
        'SW YMz1K 10x1,5': 18.7,
        'SW YMz1K 12x4': 22.6,
        'SW Y(E)Mz1K (4+10)x1,5': 20.4,
        'SW YMz1K (4+26)x1,5': 25.4,
        'SW Y(E)Mz1K (6+7x4)x1,5': 28.4,
        'SW S-Y(E)Mz1K (28+4x4)x1,5': 32,
        'SW S-Y(E)Mz1K (34+7x4)x0,8': 33.3
    },
    'SW 25kV': {
        'SW Z1O-YMz1Kas EMC 1x2x1,5+1,5': 17.0,
        'SW Z1O-YMz1Kas EMC 2x1,5+1,5': 16.8,
        'SW Z1O-YMz1Kas EMC 2x2,5+2,5': 17.8,
        'SW Z1O-YMz1Kas EMC 2x4+4': 19.1,
        'SW Z1O-YMz1Kas EMC 2x6+6': 20.0,
        'SW Z1O-YMz1Kas EMC 2x16+16': 24.7,
        'SW Z1O-YMz1Kas EMC 4x1,5+1,5': 17.7,
        'SW Z1O-YMz1Kas EMC 4x2,5+2,5': 18.6,
        'SW Z1O-YMz1Kas EMC 4x4+4': 19.9,
        'SW Z1O-YMz1Kas EMC 4x6+6': 21.3,
        'SW Z1O-YMz1Kas EMC 7x1,5+1,5': 19.3,
        'SW Z1O-YMz1Kas EMC 7x4+4': 22.0,
        'SW Z1O-YMz1Kas EMC 10x1,5': 21.9,
        'SW Z1O-YMz1Kas EMC 10x2,5': 23.3,
        'SW Z1O-YMz1Kas EMC 14x1,5+1,5': 23.4,
        'SW Z1O-YMz1Kas EMC (12x2)x1,5': 30.3,
        'SW Z1O-YMz1Kas EMC 30x1,5+1,5': 29.0,
        'SW Z1O-YMz1Kas EMC 34x1,5+1,5': 30.2,
        'SW Z1O-YMz1Kas EMC (24x2)x1,5': 47.5,
        'SW Z1O-YMz1Kas EMC 36x2x1,5+1,5': 37.5,
        'SW Z1O-YMz1Kas EMC 62x1,5+1,5': 45.2
    },
    'SW Montage': {
        'SW YMz1K 1x0,75': 7.2,
        'SW YMz1K 1x1,5': 7.7,
        'SW YMz1K 1x2,5': 8.6,
        'SW YMz1K 1x4': 9.8,
        'SW YMz1K 1x6': 10.5
    },
    'SW rubber/koper': {
        'BMqK 0,6/0,6 kV 1x2,5': 14.5,
        'BMqK 0,6/0,6 kV 1x16': 13.5,
        'BMqK 0,6/0,6 kV 1x50': 19.7,
        'BMqK 0,6/0,6 kV 1x70 AL': 21.0,
        'BMqK 0,6/0,6 kV 1x120': 25.4,
        'BMqK 0,6/0,6 kV 1x150 AL': 28.0,
        'BMqK 0,6/0,6 kV 1x16(2)': 15.4
    },
    'SW HO7 rubber': {
        'SW 07ZZ-F 4 G 2,5': 19.5,
        'SW 07ZZ-F 5 x 2,5': 21.0
    },
    'SW rubber EMC': {
        'SW 07ZZQ-F EMC 1x2x1,5': 17.7,
        'SW 07ZZQ-F EMC 4 G 4': 25.7,
        'SW 07ZZQ-F EMC 7 G 2,5': 26.0,
        'SW 07BQQ-F EMC 1x2x1,5': 29.2,
        'SW 07ZZQ-F EMC 12 G 2,5': 17.7,
        'SW 07BQQ-F EMC 4 G 4': 25.7,
        'SW 07BQQ-F EMC 7 G 2,5': 26.0,
        'SW 07BQQ-F EMC 12 G 2,5': 29.2
    },
    'SW Eurobalise': {
        'SW PHOPaszh-af-dwd 1x2x2': 20.0
    },
    'SW systeemkabel': {
        'SW PHOHas-2af (4x2)x1,3': 22.3,
        'SW PHOHas-2af (10x2)x1,3': 28.5,
        'SW PHOHas-2af (14x2)x1,3': 30.7,
        'SW PHOHas-2af (18x2)x1,3': 34.4,
        'SW A-3GF2Y-OZ 4x2,5': 21.7,
        'SW Z1O-YMz1K EMC 1x2x0,5': 13.9
    },
    'EV Laag': {
        'VO-YMvKas Dca 2x1,5 Dca': 16.8,
        'VO-YMvKas Dca 3x1,5 Dca': 17.0,
        'VO-YMvKas Dca 4x1,5 Dca': 14.1,
        'VO-YMvKas Dca 5x1,5 Dca': 19.0,
        'VO-YMvKas Dca 6x1,5 Dca': 19.1,
        'VO-YMvKas Dca 7x1,5 Dca': 20.2,
        'VO-YMvKas Dca 8x1,5 Dca': 23.0,
        'VO-YMvKas Dca 10x1,5 Dca': 23.0,
        'VO-YMvKas Dca 12x1,5 Dca': 22.2,
        'VO-YMvKas Dca 14x1,5 Dca': 23.1,
        'VO-YMvKas Dca 16x1,5 Dca': 25.2,
        'VO-YMvKas Dca 19x1,5 Dca': 26.0,
        'VO-YMvKas Dca 24x1,5 Dca': 28.6,
        'VO-YMvKas Dca 30x1,5 Dca': 30.6,
        'VO-YMvKas Dca 37x1,5 Dca': 30.6,
        'VO-YMvKas Dca 2x2,5': 17.7,
        'VO-YMvKas Dca 3x2,5': 18.0,
        'VO-YMvKas Dca 4x2,5': 18.6,
        'VO-YMvKas Dca 5x2,5': 19.9,
        'VO-YMvKas Dca 6x2,5': 19.9,
        'VO-YMvKas Dca 7x2,5': 20.2,
        'VO-YMvKas Dca 8x2,5': 21.4,
        'VO-YMvKas Dca 10x2,5': 24.9,
        'VO-YMvKas Dca 12x2,5': 23.7,
        'VO-YMvKas Dca 14x2,5': 24.7,
        'VO-YMvKas Dca 16x2,5': 27.0,
        'VO-YMvKas Dca 19x2,5': 29.0,
        'VO-YMvKas Dca 24x2,5': 31.1,
        'VO-YMvKas Dca 30x2,5': 33.3,
        'VO-YMvKas Dca 37x2,5': 33.6,
        'VO-YMvKas Dca 2x4': 18.8,
        'VO-YMvKas Dca 2x6': 20.2,
        'VO-YMvKas Dca 2x10': 23.7,
        'VO-YMvKas Dca 2x16': 25.8,
        'VO-YMvKas Dca 3x1,5': 17,
        'VO-YMvKas Dca 2x4': 18.8,
        'VO-YMvKas Dca 3x4': 19.9,
        'VO-YMvKas Dca 4x4': 20.0,
        'VO-YMvKas Dca 5x4': 21.1,
        'VO-YMvKas Dca 7x4': 21.8,
        'VO-YMvKas Dca 2x6': 20.2,
        'VO-YMvKas Dca 3x6': 20.7,
        'VO-YMvKas Dca 4x6': 21.3,
        'VO-YMvKas Dca 5x6': 23.0,
        'VO-YMvKas Dca 6x6': 23.5,
        'VO-YMvKas Dca 2x10': 23.7,
        'VO-YMvKas Dca 3x10': 24.4,
        'VO-YMvKas Dca 4x10': 26.2
    },
    'EV Hoog': {
        'VG-YMvKas Dca 2x16': 25.0,
        'VG-YMvKas Dca 2x25': 28.4,
        'VG-YMvKas Dca 2x35': 29.5,
        'VG-YMvKas Dca 2x50': 32.3,
        'VG-YMvKas Dca 2x70': 36.2,
        'VG-YMvKas Dca 2x95': 40.0,
        'VG-YMvKas Dca 3x16': 26.0,
        'VG-YMvKas Dca 3x25': 29.7,
        'VG-YMvKas Dca 3x35': 28.8,
        'VG-YMvKas Dca 3x50': 31.1,
        'VG-YMvKas Dca 3x70': 35.5,
        'VG-YMvKas Dca 3x95': 39.2,
        'VG-YMvKas Dca 4x16': 27.7,
        'VG-YMvKas Dca 4x25': 31.9,
        'VG-YMvKas Dca 4x35': 34.7,
        'VG-YMvKas Dca 4x50': 34.9,
        'VG-YMvKas Dca 4x70': 33.0,
        'VG-YMvKas Dca 4x95': 36.6,
        'VG-YMvKas Dca 4x240': 63.9
    },
    'Telecom': {
        'HDPE 40mm': 44.0,
        '12x7/3,5 DB': 44.0,
        '2xx7/3,5 DB': 16.0,
        '4x7/3,5 DB': 20.0,
        'PPCuPBaf dlwd EMC 10x4x0,8': 27.6,
        'PPCuPBaf dlwd EMC 20x4x0,8': 33.4,
        'PPCuPBaf dlwd EMC 30x4x0,8': 40.0,
        'GPEW Norm 92 - 1x4x0,5': 16.5,
        'GPEW Norm 92 - 6x4x0,5': 20.8,
        'GPEW Norm 92 - 12x4x0,5': 24.2,
        'GPEW Norm 92 - 15x4x0,5': 25.3,
        'GPEW Norm 92 - 25x4x0,5': 29.5,
        'GPEW Norm 92 - 50x4x0,5': 36.2,
        'MD 12x7/3,5': 44.0
    },
    'Overig': {
        '4x4 VMGMvKas': 20.0,
        '2x16 NGKB': 16.0,
        'HDPE 40': 44.0,
        '48x9/125SM': 16.0,
        'Placeholder': 10.0,
        'Koker-in-koker': 100.0
    }
}



# Titel en subtitel
st.title("K&L - Vullingsgraad")
st.subheader("Applicatie om de vullingsgraad te bepalen")
st.write(
    "Dit is een applicatie die aan de hand van gegeven koker/buis en kabels aangeeft "
    "wat de vullingsgraad is van de koker/buis."
)


def sync_kabel_soort(i):
    """Zorgt dat kabel_soort geldig is binnen gekozen categorie."""
    cat = st.session_state[f'kabel_categorie_{i}']
    beschikbare = list(kabels[cat].keys())

    if st.session_state.get(f'kabel_soort_{i}') not in beschikbare:
        st.session_state[f'kabel_soort_{i}'] = beschikbare[0]


def sync_diameter(i):
    """Zet diameter op basis van categorie + kabelsoort."""
    cat = st.session_state[f'kabel_categorie_{i}']
    soort = st.session_state[f'kabel_soort_{i}']
    st.session_state[f'diameter_{i}'] = kabels[cat][soort]


def init_aantal_state(i):
    """Initialiseer model-state + widget-state voor aantal."""
    value_key = f'aantal_value_{i}'
    top_key = f'aantal_top_{i}'
    result_key = f'aantal_result_{i}'

    if value_key not in st.session_state:
        st.session_state[value_key] = 1

    if top_key not in st.session_state:
        st.session_state[top_key] = st.session_state[value_key]

    if result_key not in st.session_state:
        st.session_state[result_key] = st.session_state[value_key]


def sync_aantal_from_top(i):
    """Synchroniseer aantal vanuit invoerblok naar model + resultatenblok."""
    value_key = f'aantal_value_{i}'
    top_key = f'aantal_top_{i}'
    result_key = f'aantal_result_{i}'

    st.session_state[value_key] = st.session_state[top_key]
    st.session_state[result_key] = st.session_state[value_key]


def sync_aantal_from_result(i):
    """Synchroniseer aantal vanuit resultatenblok naar model + invoerblok."""
    value_key = f'aantal_value_{i}'
    top_key = f'aantal_top_{i}'
    result_key = f'aantal_result_{i}'

    st.session_state[value_key] = st.session_state[result_key]
    st.session_state[top_key] = st.session_state[value_key]


def get_restkleur(vullingsgraad):
    """Bepaal kleur van resterende ruimte in de pie chart."""
    if vullingsgraad > 0.75:
        return '#ff0000'
    elif vullingsgraad > 0.50:
        return '#fff600'
    else:
        return '#ffcc99'


def toon_vullingsmelding(koker_naam, vullingsgraad):
    """Toon statusmelding met passende kleur/intensiteit."""
    if vullingsgraad > 1.0:
        st.error(f"{koker_naam} is kleiner dan ingevoerde kabels (>100%).")
    elif vullingsgraad > 0.75:
        st.warning(f"{koker_naam} is meer dan 75% gevuld.")
    elif vullingsgraad > 0.50:
        st.info(f"{koker_naam} is meer dan 50% gevuld.")


# =========================
# 1. KOKERS CONFIGUREREN
# =========================
st.markdown("---")
st.header("1. Koker/buis configureren")

num_kokers = st.number_input(
    "Selecteer het aantal kokers/buizen",
    min_value=1,
    max_value=3,
    step=1,
    value=1
)

gekozen_kokers = []

for k in range(int(num_kokers)):
    st.markdown(f"#### Koker/Buis {k+1}")

    col1, col2 = st.columns([1.4, 2.6])

    with col1:
        koker_naam = st.text_input(
            "Naam koker/buis",
            value=f"Koker {k+1}",
            key=f"koker_naam_{k}"
        )

    with col2:
        koker_type = st.selectbox(
            "Type koker/buis",
            list(kokers.keys()),
            key=f"koker_type_{k}"
        )

    gekozen_kokers.append({
        "id": k,
        "naam": koker_naam,
        "type": koker_type,
        "oppervlakte": kokers[koker_type]
    })

    st.caption(f"Oppervlakte: {kokers[koker_type]:.2f} mm²")


# =========================
# 2. KABELS INVOEREN
# =========================
st.markdown("---")
st.header("2. Kabels invoeren")

num_inputs = st.number_input(
    "Selecteer het aantal kabeltypes in de koker/buis",
    min_value=1,
    max_value=100,
    step=1,
    value=1
)

kabel_categorieen = []
kabels_soorten = []
namen = []
diameters = []
oppervlaktes_kabels = []
aantallen = []
koker_toewijzing = []

st.markdown("#### Kabelregels")

# Headerregel
h1, h2, h3, h4, h5, h6 = st.columns([1.4, 2.8, 1.0, 1.4, 1.8, 1.0])
with h1:
    st.markdown("**Categorie**")
with h2:
    st.markdown("**Type kabel**")
with h3:
    st.markdown("**Diameter**")
with h4:
    st.markdown("**Naar koker/buis**")
with h5:
    st.markdown("**Naam**")
with h6:
    st.markdown("**Aantal**")

for i in range(int(num_inputs)):
    if f'kabel_categorie_{i}' not in st.session_state:
        st.session_state[f'kabel_categorie_{i}'] = list(kabels.keys())[0]

    if f'kabel_soort_{i}' not in st.session_state:
        sync_kabel_soort(i)

    if f'diameter_{i}' not in st.session_state:
        sync_diameter(i)

    if f'naam_{i}' not in st.session_state:
        st.session_state[f'naam_{i}'] = ""

    if f'koker_toewijzing_{i}' not in st.session_state:
        st.session_state[f'koker_toewijzing_{i}'] = gekozen_kokers[0]["naam"]

    init_aantal_state(i)

    col1, col2, col3, col4, col5, col6 = st.columns([1.4, 2.8, 1.0, 1.4, 1.8, 1.0])

    with col1:
        st.selectbox(
            f"Categorie {i}",
            list(kabels.keys()),
            key=f'kabel_categorie_{i}',
            on_change=lambda idx=i: (sync_kabel_soort(idx), sync_diameter(idx)),
            label_visibility="collapsed"
        )
        kabel_categorieen.append(st.session_state[f'kabel_categorie_{i}'])

    sync_kabel_soort(i)

    with col2:
        cat = st.session_state[f'kabel_categorie_{i}']
        st.selectbox(
            f"Type kabel {i}",
            list(kabels[cat].keys()),
            key=f'kabel_soort_{i}',
            on_change=lambda idx=i: sync_diameter(idx),
            label_visibility="collapsed"
        )
        kabels_soorten.append(st.session_state[f'kabel_soort_{i}'])

    with col3:
        diameter = st.number_input(
            f"Diameter {i}",
            min_value=0.0,
            step=0.1,
            key=f'diameter_{i}',
            label_visibility="collapsed"
        )
        diameters.append(diameter)

    with col4:
        beschikbare_kokernamen = [k["naam"] for k in gekozen_kokers]

        if st.session_state[f'koker_toewijzing_{i}'] not in beschikbare_kokernamen:
            st.session_state[f'koker_toewijzing_{i}'] = beschikbare_kokernamen[0]

        st.selectbox(
            f"Naar koker/buis {i}",
            beschikbare_kokernamen,
            key=f'koker_toewijzing_{i}',
            label_visibility="collapsed"
        )
        koker_toewijzing.append(st.session_state[f'koker_toewijzing_{i}'])

    with col5:
        naam = st.text_input(
            f"Naam {i}",
            key=f'naam_{i}',
            placeholder=f"Kabel {i+1}",
            label_visibility="collapsed"
        )
        namen.append(naam)

    with col6:
        st.number_input(
            f"Aantal {i}",
            min_value=0,
            step=1,
            key=f'aantal_top_{i}',
            on_change=lambda idx=i: sync_aantal_from_top(idx),
            label_visibility="collapsed"
        )

        aantal = st.session_state[f'aantal_value_{i}']
        aantallen.append(aantal)

        oppervlakte_kabel = 0.25 * math.pi * (diameter ** 2) * aantal
        oppervlaktes_kabels.append(oppervlakte_kabel)


# =========================
# 3. RESULTATEN PER KOKER
# =========================
st.markdown("---")
st.header("3. Resultaten per koker/buis")

for koker in gekozen_kokers:
    koker_naam = koker["naam"]
    koker_type = koker["type"]
    oppervlakte_koker = koker["oppervlakte"]

    indices = [
        i for i in range(int(num_inputs))
        if st.session_state[f'koker_toewijzing_{i}'] == koker_naam
    ]

    kabel_namen_koker = []
    kabel_oppervlaktes_koker = []

    for i in indices:
        kabelnaam = st.session_state[f'naam_{i}'] if st.session_state[f'naam_{i}'] else f"Kabel {i+1}"
        actueel_aantal = st.session_state[f'aantal_value_{i}']
        actuele_diameter = st.session_state[f'diameter_{i}']
        actuele_oppervlakte = 0.25 * math.pi * (actuele_diameter ** 2) * actueel_aantal

        kabel_namen_koker.append(kabelnaam)
        kabel_oppervlaktes_koker.append(actuele_oppervlakte)

    totale_oppervlakte_kabels = sum(kabel_oppervlaktes_koker)
    vullingsgraad = totale_oppervlakte_kabels / oppervlakte_koker if oppervlakte_koker > 0 else 0.0
    resterende_oppervlakte = max(0.0, oppervlakte_koker - totale_oppervlakte_kabels)

    st.markdown("---")
    st.subheader(koker_naam)

    left, right = st.columns([1.35, 1.0])

    with left:
        st.caption(f"{koker_type}")

        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric("Oppervlakte koker/buis", f"{oppervlakte_koker:.0f} mm²")
        with m2:
            st.metric("Kabeloppervlakte", f"{totale_oppervlakte_kabels:.0f} mm²")
        with m3:
            st.metric("Vullingsgraad", f"{vullingsgraad:.1%}")

        toon_vullingsmelding(koker_naam, vullingsgraad)

        st.markdown("##### Kabels in deze koker/buis")

        if indices:
            th1, th2, th3 = st.columns([2.0, 3.6, 1.4])
            with th1:
                st.markdown("**Kabelnaam**")
            with th2:
                st.markdown("**Kabeltype**")
            with th3:
                st.markdown("**Bewerkt aantal**")

            for i in indices:
                kabelnaam = st.session_state[f'naam_{i}'] if st.session_state[f'naam_{i}'] else f"Kabel {i+1}"
                kabeltype = st.session_state[f'kabel_soort_{i}']

                c1, c2, c3 = st.columns([2.0, 3.6, 1.4])

                with c1:
                    st.write(kabelnaam)

                with c2:
                    st.write(kabeltype)

                with c3:
                    st.number_input(
                        f"Bewerkt aantal {i}",
                        min_value=0,
                        step=1,
                        key=f'aantal_result_{i}',
                        on_change=lambda idx=i: sync_aantal_from_result(idx),
                        label_visibility="collapsed"
                    )
        else:
            st.info("Geen kabels toegewezen aan deze koker/buis.")

    with right:
    fig, ax = plt.subplots()

    overvol = totale_oppervlakte_kabels >= oppervlakte_koker

    if not overvol:
        labels = kabel_namen_koker + ["Resterende ruimte"]
        sizes = kabel_oppervlaktes_koker + [resterende_oppervlakte]
    else:
        labels = kabel_namen_koker
        sizes = kabel_oppervlaktes_koker

    if len(kabel_namen_koker) > 0:
        if overvol:
            # alles rood bij overvol
            colors = ['#ff0000' for _ in kabel_namen_koker]
        else:
            # normaal groen verloop
            colors = [
                '#%02x%02x%02x' % (0, int(255 - 255 * j / len(kabel_namen_koker)), 0)
                for j in range(len(kabel_namen_koker))
            ]
    else:
        colors = []

    # Alleen restkleur toevoegen als het NIET overvol is
    if not overvol:
        colors.append(get_restkleur(vullingsgraad))

    if sum(sizes) > 0:
        ax.pie(
            sizes,
            labels=labels,
            colors=colors,
            autopct='%1.1f%%',
            startangle=90
        )
        ax.axis('equal')

        if overvol:
            ax.set_title(f"{koker_naam} - OVERVOL", color='red')
        else:
            ax.set_title(f"Verdeling {koker_naam}")

        st.pyplot(fig)
    else:
        ax.axis('off')
        ax.text(0.5, 0.5, "Geen data", ha='center', va='center')
        st.pyplot(fig)
