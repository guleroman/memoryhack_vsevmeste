from read_write import writeHtml
from key_generation import generate_key
from parseMap import getNewMap

def generationPage(all_entity):

    newMap = getNewMap(all_entity['Units'])

    markup = f'''<!DOCTYPE html>
    <html style="font-family: FontAwesome;" lang="en">

    <head>
        <base href="http://vsevmesteru.ru/">

        <link rel="apple-touch-icon" sizes="180x180"
        href="static/images/apple-touch-icon.png">
        <link rel="canonical" href="http://vsevmesteru.ru/">
        <link rel="icon" type="image/png" sizes="16x16"
        href="static/images/favicon-16x16.png">
        <link rel="icon" type="image/png" sizes="192x192"
        href="static/images/android-chrome-192x192.png">
        <link rel="icon" type="image/png" sizes="192x192"
        href="static/images/favicon-192x192.png">
        <link rel="icon" type="image/png" sizes="32x32"
        href="static/images/favicon-32x32.png">
        <link rel="manifest" href="static/site.webmanifest">
        <link rel="shortcut icon" href="static/images/favicon.ico">
        <meta charset="utf-8">
        <meta content="ie=edge" http-equiv="x-ua-compatible">
        <meta name="apple-mobile-web-app-title" content="ВсеВместе - {all_entity['Name']}">
        <meta name="application-name" content="ВсеВместе - {all_entity['Name']}">
        <meta name="description" content="ВсеВместе - {all_entity['Name']}">
        <meta name="googlebot" content="index,follow">
        <meta name="msapplication-TileColor" content="#2b5797">
        <meta name="robots" content="index,follow">
        <meta name="theme-color" content="#2d3748">
        <meta name="viewport" content="width=device-width,initial-scale=0.4, maximum-scale=0.4">
        <meta name="twitter:card" content="summary_large_image">
        <meta name="twitter:creator" content="@guleroman">
        <meta name="twitter:site" content="@vse_vmeste_bot">
        <meta property="og:description" content="ВсеВместе - {all_entity['Name']}">
        <meta property="og:image:height" content="844">
        <meta property="og:image:width" content="1500">
        <meta property="og:locale" content="en_US">
        <meta property="og:site_name" content="ВсеВместе - {all_entity['Name']}">
        <meta property="og:title" content="ВсеВместе - {all_entity['Name']}">
        <meta property="og:type" content="website">
        <meta property="og:url" content="http://vsevmesteru.ru/">
        <title>ВсеВместе - {all_entity['Name']}</title>
        <link href="static/css/main.6f70e7c3.chunk.css" rel="stylesheet"
        type="text/css">
        <link href="static/css/2.7d8cb3b4.chunk.css" rel="stylesheet"
        type="text/css">
        <link href="static/css/style_1.css" rel="stylesheet" type="text/css">
    </head>

    <body>
        <main class="bg-gray-300" id="root" style="min-width:520px"><span id="d3-tip"></span>
        <header class="h-16">
            <div class="bg-white fixed h-16 bg-white shadow-md top-0 inset-x-0" style="z-index: 20000;"></div>
            <div class="container mx-auto flex fixed h-16 top-0 inset-x-0 
            items-center justify-between p-2" style="z-index: 200000;">
            <div class="pl-0 flex flex-row items-center"><a href="/"><button
                    class="pl-4 py-2 font-bold flex items-center flex-row"
                    type="button"><img src="../static/images/logoo.png" class="rounded-lg" style="max-height: 50px;margin: 1rem; ">
                    </svg>
                    <span class="hidden lg:inline-block mr-2 xl:text-xl
                    text-gray-800 hover:text-brand" style="font-size: 2rem;">ВсеВместе</span></button></a>
            </div>
            <div class="w-40">
            </div>
            <div class="w-40">
            </div>
            </div>
            <div class="relative">
            <div aria-hidden="true" style="opacity: 1; transition: opacity 200ms
                linear 0s;">
                <div class="bg-brand fixed w-full"
                style="height: 2px; left: 0px; margin-left: -100%; top: 63px;
                transition: margin-left 200ms linear 0s; z-index: 9;">
                <div class="absolute block h-full right-0 shadow-inner"
                    style="opacity: 1; transform: rotate(3deg) translate(0px, -4px);
                    width: 100px;"></div>
                </div>
            </div>
            </div>
        </header>
        <div class="flex flex-1">
            <div class="flex container mx-auto flex-col">
            <h1 style="left: -9999px; position: absolute; top: -9999px;">ВсеВместе - {all_entity['Name']}</h1>
            <section class="flex flex-col xl:flex-row mb-16 mt-8">
                <div id="overlay">
                <div class="cv-spinner">
                    <span class="spinner"></span>
                </div>
                </div>
                <div id="overlay_pop_up" style="display: none;">
                <div style="display: flex;justify-content: center;align-items: center;" class="">
                <span style="max-width: 600px;height: auto;margin: 5rem;" class="h-auto bg-white rounded-lg shadow">
                    <div class="flex flex-row lg:flex-row" style="justify-content: end;">
                    <button onclick='$("#overlay_pop_up").attr("style","display: none;")' onmouseover="this.style.backgroundColor='#AB0606';" onmouseout="this.style.backgroundColor='lightcoral';" style="border-radius: 100px; padding: 4px 10px; font-family: revert; align-content: space-around; background-color: lightcoral; position: relative;" class="shadow-inner absolute inline-flex justify-center
                        items-baseline text-sm px-2 rounded top-0
                        right-0 text-white bg-teal-600">X</button>
                    </div>
                    <div id="overlay_pop_up_text" class="" style="text-align: center;padding-left: 1rem; padding-right: 1rem;padding-bottom: 1rem;">Привет медвед</div>
                </span>
                </div>
                </div>
            </section>
            <section class="flex flex-col xl:flex-row relative">
                <div class="xl:w-1/3 h-auto bg-white rounded-lg shadow mx-2">
                <div class="p-4 relative">
                    <div class="flex flex-row"><img id="profile_image"
                        class="rounded-lg mr-4 h-12 w-h-12"
                        src="{all_entity['Foto']}">
                    <div class="flex flex-col overflow-hidden" style="position: relative;max-width: 12rem;"><a id="acc_twitter_link" style="margin-top: 1rem;" rel="noopener
                        noreferrer" target="_blank"><span
                            class="leading-none font-semibold text-xl
                            hover:text-brand" id="acc_name">{all_entity['Name']}</span></a><a id="acc_username_2" rel="noopener
                        noreferrer"
                        target="_blank">
                        <h2 id="acc_username" class="font-medium text-lg
                            text-gray-500
                            hover:text-brand"></h2>
                        </a>
                        <div>
                        <p id="acc_bio" style="font-style: italic;" class="break-words text-gray-800 mt-4 leading-tight">«..{all_entity['Description']}»</p>
                        </div>
                    </div>
                    </div>
                    
                    <div class="mt-4">
                    <ul>
                        <li><span><svg aria-hidden="true" focusable="false"
                            data-prefix="fas" data-icon="calendar"
                            class="svg-inline--fa fa-calendar fa-w-14 fa-fw
                            text-brand" role="img"
                            xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448
                            512" aria-describedby="tooltip:13"
                            data-reach-tooltip-trigger="">
                            <path fill="currentColor"
                                d="M12 192h424c6.6 0 12 5.4 12 12v260c0 26.5-21.5
                                48-48 48H48c-26.5 0-48-21.5-48-48V204c0-6.6 5.4-12
                                12-12zm436-44v-36c0-26.5-21.5-48-48-48h-48V12c0-6.6-5.4-12-12-12h-40c-6.6
                                0-12 5.4-12 12v52H160V12c0-6.6-5.4-12-12-12h-40c-6.6
                                0-12 5.4-12 12v52H48C21.5 64 0 85.5 0 112v36c0 6.6
                                5.4 12 12 12h424c6.6 0 12-5.4 12-12z" style="color: #ff606c;">
                            </path>
                            </svg></span> <time datetime="2009-04-18T13:46:38.000Z"></time>
                        <a class="text-gray-800" id="acc_join_date">{all_entity['Date_1']}</a>г. - <a class="text-gray-800" id="acc_death_date">{all_entity['Date_2']}</a>г.</li>
                        <li><span><svg aria-hidden="true" focusable="false"
                            data-prefix="fas" data-icon="map-marker"
                            class="svg-inline--fa fa-map-marker fa-w-12 fa-fw
                            text-brand" role="img"
                            xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384
                            512" aria-describedby="tooltip:16"
                            data-reach-tooltip-trigger="">
                            <path fill="currentColor"
                                d="M172.268 501.67C26.97 291.031 0 269.413 0 192 0
                                85.961 85.961 0 192 0s192 85.961 192 192c0
                                77.413-26.97 99.031-172.268 309.67-9.535
                                13.774-29.93 13.773-39.464 0z" style="color: #ff606c;">
                            </path>
                            </svg></span> <a class="text-gray-800" id="acc_location">{all_entity['City']}</a></li>
                            <li><span><svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="address-card" class="svg-inline--fa fa-address-card fa-w-18 fa-fw
                            text-brand" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576
                            512" aria-describedby="tooltip:14" data-reach-tooltip-trigger="">
                            <path fill="currentColor" d="M528 32H48C21.5 32 0 53.5 0 80v352c0 26.5 21.5 48
                                48 48h480c26.5 0 48-21.5
                                48-48V80c0-26.5-21.5-48-48-48zm-352 96c35.3 0 64
                                28.7 64 64s-28.7 64-64 64-64-28.7-64-64 28.7-64
                                64-64zm112 236.8c0 10.6-10 19.2-22.4 19.2H86.4C74
                                384 64 375.4 64 364.8v-19.2c0-31.8 30.1-57.6
                                67.2-57.6h5c12.3 5.1 25.7 8 39.8 8s27.6-2.9
                                39.8-8h5c37.1 0 67.2 25.8 67.2 57.6v19.2zM512 312c0
                                4.4-3.6 8-8 8H360c-4.4 0-8-3.6-8-8v-16c0-4.4 3.6-8
                                8-8h144c4.4 0 8 3.6 8 8v16zm0-64c0 4.4-3.6 8-8
                                8H360c-4.4 0-8-3.6-8-8v-16c0-4.4 3.6-8 8-8h144c4.4 0
                                8 3.6 8 8v16zm0-64c0 4.4-3.6 8-8 8H360c-4.4
                                0-8-3.6-8-8v-16c0-4.4 3.6-8 8-8h144c4.4 0 8 3.6 8
                                8v16z" style="color: #ff606c;">
                            </path>
                            </svg></span> <a
                            href="https://pamyat-naroda.ru/warunit/{all_entity['Units']}/"
                            rel="noopener noreferrer" target="_blank"><span
                            class="text-gray-800 hover:text-brand">{all_entity['Units']}</span></a></li>  
                    </ul>
                    </div>
                </div>
                </div>
                <div class="mt-4 xl:mt-0 xl:w-2/3 h-auto bg-white rounded-lg shadow
                mx-2 relative">
                <div class="w-full flex flex-col relative">
                    <h2 class="font-semibold ml-4 mt-2 mb-4 text-lg">Боевой путь</h2>
                    <div style="overflow: scroll;position: relative;min-height: 350px;margin-left: 1rem;margin-right: 0.5rem;">{newMap}</div>
                </div>
                </div>
            </section>
            <section class="flex flex-col lg:flex-row mt-4">
                <div class="lg:w-1/3 h-auto bg-white rounded-lg shadow mx-2
                relative">
                <div class="w-full flex flex-col relative">
                    <h2 class="font-semibold ml-4 mt-2 mb-4 text-lg">Награды</h2>
                </div>
                <div name="border_color" class="flex flex-col shadow rounded text-gray-800 p-2
                    relative border-l-4 bg-gray-100 border-purple-600" style="margin: 1rem;">
                    <div class="relative" style="padding: .5rem;">
                    <div class="flex flex-row"><img id="acc_image" class="rounded-lg mr-4 h-12 w-h-12" style="height: 5rem;" src="https://upload.wikimedia.org/wikipedia/ru/a/a8/%D0%9C%D0%B5%D0%B4%D0%B0%D0%BB%D1%8C_%C2%AB%D0%97%D0%B0_%D0%BE%D1%82%D0%B2%D0%B0%D0%B3%D1%83%C2%BB_%28%D0%A0%D0%A4%29.png">
                        <div class="flex flex-col overflow-hidden max-w-2xs
                        lg:max-w-full xl:max-w-2xs"><a id="acc_twitter_link" href="https://twitter.com/WKU_Inowroclaw" rel="noopener
                            noreferrer" target="_blank"><span class="break-all leading-none font-semibold text-xl
                            hover:text-brand whitespace-no-wrap" id="acc_name">Медаль «За отвагу»</span></a>
                            <a id="acc_username_2" rel="noopener
                            noreferrer" target="_blank">
                            <h2 id="acc_username" class="font-medium text-lg
                            text-gray-500
                            hover:text-brand">1944г.</h2>
                        </a></div>
                    </div>
                    </div>
                </div>
                </div>
                <div class="lg:w-1/3 h-auto bg-white rounded-lg shadow mx-2
                relative">
                <div class="w-full flex flex-col relative">
                    <h2 class="font-semibold ml-4 mt-2 mb-4 text-lg">Фотографии</h2>
                </div>
                <div class="p-2">
                    <div id="messageBoard" class="flex flex-col md:flex-row
                    md:flex-wrap items-center
                    md:items-start justify-around m-2 " style="/*! justify-content: center; */">
                    <div name="border_color" class="flex flex-col shadow rounded text-gray-800 p-2
                        relative bg-gray-100" style="margin: .5rem; width:auto;height: auto;">
                        <div class="relative" style="">
                            <div class="flex flex-col" style="flex-direction: column;"><img id="acc_image" style="max-height: 150px;width: auto;" class="rounded-lg " src="https://vr-vyksa.ru/media/images/37_ilktlts.max-1200x800.jpg">
                            </div>
                        </div>
                        </div><div name="border_color" class="flex flex-col shadow rounded text-gray-800 p-2
                        relative bg-gray-100" style="margin: .5rem; width:auto;height: auto;">
                        <div class="relative" style="">
                            <div class="flex flex-col" style="flex-direction: column;"><img id="acc_image" style="max-height: 150px;width: auto;" class="rounded-lg " src="https://cs6.pikabu.ru/post_img/big/2014/04/07/6/1396860636_1421982419.jpg">
                            </div>
                        </div>
                        </div><div name="border_color" class="flex flex-col shadow rounded text-gray-800 p-2
                        relative bg-gray-100" style="margin: .5rem; width:auto;height: auto;">
                        <div class="relative" style="">
                            <div class="flex flex-col" style="flex-direction: column;"><img id="acc_image" style="max-height: 150px;width: auto;" class="rounded-lg " src="https://www.ugra-news.ru/upload/iblock/c77/1128887953.jpg">
                            </div>
                        </div>
                        </div><div name="border_color" class="flex flex-col shadow rounded text-gray-800 p-2
                        relative bg-gray-100" style="margin: .5rem; width:auto;height: auto;">
                        <div class="relative" style="">
                            <div class="flex flex-col" style="flex-direction: column;"><img id="acc_image" style="max-height: 150px;width: auto;" class="rounded-lg " src="https://www.penza-press.ru/uploads/news/2020/01_2020/lenta/28/458675476.jpg">
                            </div>
                        </div>
                        </div>
                        </div>
                    </div>
                </div>
                <div class="mt-4 lg:mt-0 lg:w-1/3 h-auto bg-white rounded-lg shadow
                mx-2 relative"><span
                    class="absolute left-0 top-1/2 -ml-4 sm:-ml-2 font-semibold
                    text-gray-400 tracking-wide"
                    style="transform: rotate(-90deg);"></span><span
                    class="absolute bottom-0 left-1/2 mb-1 sm:mb-2 font-semibold
                    text-gray-400 tracking-wide w-1/2"
                    style="margin-left: -16.5px;"></span>
                <div class="w-full flex flex-col relative">
                    <h2 class="font-semibold ml-4 mt-2 mb-4 text-lg">Архивные документы</h2>
                </div>
                <div name="border_color" class="flex flex-col shadow rounded text-gray-800 p-2
                    relative border-l-4 bg-gray-100 border-purple-600" style="margin: 1rem;">
                    <div class="relative" style="padding: .5rem;">
                <a id="acc_twitter_link" rel="noopener
                            noreferrer" target="_blank" href="https://pamyat-naroda.ru/documents/view/?id=114203978"><span id="acc_name" class=" leading-none font-semibold
                                hover:text-brand">Выписка из журнала боевых действий батареи ПА 130 гв. сп за период с 01.11.44 по 01.12.44</span></a>        
                    </div>
                    </div>
                </div>
            </section>

            </div>
        </div>
        <footer class="bg-white py-8 mt-8 lg:mt-16 w-full">
            <div class="container mx-auto px-4">

            <nav class="flex flex-col sm:flex-row justify-between w-full mt-4">
                <div class="w-full">
                </div>
                <div class="w-full">
                </div>
                <div class="w-full">
                </div>
                <div class="w-full">
                </div>
                <div class="w-full">
                <p class="uppercase text-gray-400 font-medium text-lg sm:mb-2">We</p>
                <div class="text-lg">Developed on<a
                    href="https://memoryhack.ru/"
                    rel="noopener noreferrer" target="_blank" title="MemoryHack hackathon"><span
                        class="text-gray-800 hover:text-brand"> MemoryHack</span></a> by <a
                        href="https://www.github.com/guleroman"
                        rel="noopener noreferrer" target="_blank" title="guleroman's Github Profile"><span
                        class="text-gray-800 hover:text-brand">@guleroman</span></a> and <a
                        href="https://github.com/SadrikA78/"
                        rel="noopener noreferrer" target="_blank" title="SadrikA78's Github Profile"><span
                            class="text-gray-800 hover:text-brand">@SadrikA78</span></a></div>
                </div>
            </nav>
            </div>
        </footer>
        </main>
        
        <!--===============================================================================================-->
        <script src="static/js/imageResize.js"></script>
        <!--===============================================================================================-->
        <script src="static/vendor/jquery/jquery-3.2.1.min.js"></script>
        <!--===============================================================================================-->
        <script src="static/js/blockscroll.js"></script>
        <!--===============================================================================================-->

    </body>

    </html>'''

    markup = deEmojify(markup)

    # print (newMap)
    print ("_"*30)
    # print (markup)

    key = generate_key()
    writeHtml(markup,key+".html")
    return({"status_code":200,"key":key})


def deEmojify(inputString):
    returnString = ""
    for character in inputString:
        try:
            character.encode("ascii")
            returnString += character
        except:
            try:
                character.encode("cp1251")
                returnString += character
            except:
                returnString += ''
    return returnString