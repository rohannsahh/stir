# import zipfile

# def create_proxyauth_extension(proxy_host, proxy_port, proxy_username, proxy_password, scheme='http', plugin_path=None):
#     if plugin_path is None:
#         plugin_path = 'proxy_auth_plugin.zip'

#     manifest_json = """
#     {
#         "version": "1.0.0",
#         "manifest_version": 2,
#         "name": "Proxy Auth Extension",
#         "permissions": [
#             "proxy",
#             "tabs",
#             "unlimitedStorage",
#             "storage",
#             "<all_urls>",
#             "webRequest",
#             "webRequestBlocking"
#         ],
#         "background": {
#             "scripts": ["background.js"]
#         },
#         "minimum_chrome_version":"22.0.0"
#     }
#     """

#     background_js = f"""
#     var config = {{
#             mode: "fixed_servers",
#             rules: {{
#               singleProxy: {{
#                 scheme: "{scheme}",
#                 host: "{proxy_host}",
#                 port: parseInt({proxy_port})
#               }},
#               bypassList: ["localhost"]
#             }}
#           }};
#     chrome.proxy.settings.set({{value: config, scope: "regular"}}, function() {{}});
#     function callbackFn(details) {{
#         return {{
#             authCredentials: {{
#                 username: "{proxy_username}",
#                 password: "{proxy_password}"
#             }}
#         }};
#     }}
#     chrome.webRequest.onAuthRequired.addListener(
#                 callbackFn,
#                 {{urls: ["<all_urls>"]}},
#                 ['blocking']
#     );
#     """

#     with zipfile.ZipFile(plugin_path, 'w') as zp:
#         zp.writestr("manifest.json", manifest_json)
#         zp.writestr("background.js", background_js)

#     return plugin_path


import zipfile

proxy_host = "us-ca.proxymesh.com"
proxy_port = 31280
proxy_user = "rohan11"
proxy_pass = "rohan11"

manifest_json = """
{
   "version": "1.0.0",
   "manifest_version": 2,
   "name": "Chrome Proxy",
   "permissions": [
       "proxy",
       "tabs",
       "unlimitedStorage",
       "storage",
       "<all_urls>",
       "webRequest",
       "webRequestBlocking"
   ],
   "background": {
       "scripts": ["background.js"]
   },
   "minimum_chrome_version":"22.0.0"
}
"""

background_js = f"""
var config = {{
        mode: "fixed_servers",
        rules: {{
        singleProxy: {{
            scheme: "http",
            host: "{proxy_host}",
            port: {proxy_port}
        }},
        bypassList: ["localhost"]
        }}
    }};

chrome.proxy.settings.set({{value: config, scope: "regular"}}, function() {{}});
chrome.webRequest.onAuthRequired.addListener(
    function(details) {{
        return {{
            authCredentials: {{
                username: "{proxy_user}",
                password: "{proxy_pass}"
            }}
        }};
    }},
    {{urls: ["<all_urls>"]}},
    ["blocking"]
);
"""

# Save the files in a zip archive
pluginfile = "proxy_auth_plugin.zip"
with zipfile.ZipFile(pluginfile, "w") as zp:
    zp.writestr("manifest.json", manifest_json)
    zp.writestr("background.js", background_js)
