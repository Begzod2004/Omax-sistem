from drf_yasg import openapi


def mahsulot_olchov_query_params():
    olchov = openapi.Parameter(
        "olchov", openapi.IN_QUERY, description="olchov id si", type=openapi.TYPE_STRING)
    narx = openapi.Parameter("narx", openapi.IN_QUERY,
                             description="narx", type=openapi.TYPE_STRING)
    return [olchov, narx]


def import_export_query_params():
    mahsulot_nomi = openapi.Parameter("mahsulot_nomi", openapi.IN_QUERY, description="mahsulot_nomi",
                                      type=openapi.TYPE_STRING)
    format = openapi.Parameter(
        "format", openapi.IN_QUERY, description="format", type=openapi.TYPE_STRING)
    miqdor = openapi.Parameter(
        "miqdor", openapi.IN_QUERY, description="miqdor", type=openapi.TYPE_INTEGER)
    vaqt = openapi.Parameter("import_vaqt", openapi.IN_QUERY, description="import_vaqt format (yyyy-mm-dd)",
                             type=openapi.TYPE_INTEGER)

    return [mahsulot_nomi, format, miqdor, vaqt]


def customer_query_params():
    nomi = openapi.Parameter("nomi", openapi.IN_QUERY,
                             description="nomi", type=openapi.TYPE_STRING)
    ism_sharif = openapi.Parameter(
        "ism_sharif", openapi.IN_QUERY, description="ism_sharif", type=openapi.TYPE_STRING)
    return [nomi, ism_sharif]


def order_query_params():
    mijoz = openapi.Parameter(
        "mijoz", openapi.IN_QUERY, description="mijoz id si", type=openapi.TYPE_INTEGER)
    format = openapi.Parameter(
        "format", openapi.IN_QUERY, description="format", type=openapi.TYPE_STRING)
    buyurtma_olchov = openapi.Parameter(
        "buyurtma_olchov", openapi.IN_QUERY, description="buyurtma_olchov", type=openapi.TYPE_STRING)
    buyurtma_sana = openapi.Parameter("buyurtma_sana", openapi.IN_QUERY,
                                      description="buyurtma_sana format (yyyy-mm-dd)",
                                      type=openapi.TYPE_STRING)
    return [mijoz, format, buyurtma_sana, buyurtma_olchov]


def bonus_query_params():
    bonus_nomi = openapi.Parameter(
        "bonus_nomi", openapi.IN_QUERY, description="bonus_nomi", type=openapi.TYPE_STRING)
    bonus_miqdori = openapi.Parameter(
        "bonus_miqdori", openapi.IN_QUERY, description="bonus_miqdori", type=openapi.TYPE_STRING)
    bonus_muddati = openapi.Parameter(
        "bonus_muddati", openapi.IN_QUERY, description="bonus_muddati", type=openapi.TYPE_STRING)

    return [bonus_nomi, bonus_miqdori, bonus_muddati]


def mahsulot_query_params():
    mahsulot_nomi = openapi.Parameter(
        "mahsulot_olchov", openapi.IN_QUERY, description="mahsulot_olchov", type=openapi.TYPE_INTEGER)
    mahsulot_format = openapi.Parameter(
        "mahsulot_format", openapi.IN_QUERY, description="mahsulot_format", type=openapi.TYPE_STRING)

    return mahsulot_nomi, mahsulot_format


def mahsulot_olchov_query_params():
    olchov = openapi.Parameter("olchov", openapi.IN_QUERY, description="olchov id si", type=openapi.TYPE_STRING)
    olchov = openapi.Parameter("olchov", openapi.IN_QUERY, description="olchov", type=openapi.TYPE_STRING)
    narx = openapi.Parameter("narx", openapi.IN_QUERY, description="narx", type=openapi.TYPE_STRING)
    mahsulot_number = openapi.Parameter("mahsulot_number", openapi.IN_QUERY,
                                        description="mahsulot_number", type=openapi.TYPE_INTEGER)

    return [olchov, narx, mahsulot_number]


def worker_query_params():
    lavozim = openapi.Parameter(
        "lavozim", openapi.IN_QUERY, description="lavozim", type=openapi.TYPE_STRING)
    ism_sharif = openapi.Parameter(
        "ism_sharif", openapi.IN_QUERY, description="ism_sharif", type=openapi.TYPE_STRING)

    return [ism_sharif, lavozim]
