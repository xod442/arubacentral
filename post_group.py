'''
Sample Python Script using pycentral
2023 wookieware.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0.

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


__author__ = "@netwookie"
__credits__ = ["Rick Kauffman"]
__license__ = "Apache2"
__version__ = "0.1.1"
__maintainer__ = "Rick Kauffman"
__email__ = "rick@rickkauffman.com"
__status__ = "Alpha"

'''
# Get client connection for Aruba Central
from utility.client import get_client
from pycentral.configuration import Groups


def post_group():
    ssl_verify = True
    central = get_client()

    group_name = "bob123"
    group_password = "P@55w0rd!"
    wired_template = False
    wireless_template = False

    print("---------------Creating Group----------------------")

    groups = Groups()

    response = groups.create_group(conn=central,
                                  group_name=group_name,
                                  group_password=group_password,
                                  wired_template=wired_template,
                                  wireless_template=wireless_template)



    return(response['code'])


if __name__ == "__main__":
    response = post_group()
    print(response)
