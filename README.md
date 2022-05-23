<div id="top"></div>
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<div align="center">

<h3 align="center">apex-blocker</h3>

  <p align="center">
    A collection of scripts designed to block high latency Apex Legend servers (and maybe other game servers too).
    <br />
    <a href="https://github.com/16x16/apex-blocker/issues">Report Bug</a>
    ·
    <a href="https://github.com/16x16/apex-blocker/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a collection of scripts designed to block Apex Legends servers (or Multiplay servers in general). It's aimed at people that frequently encounter high ping servers in Apex Legends. Those scripts filter the list of servers by your specified ping threshold, and block high ping servers using Windows Firewall.  

The list of server is planned to be updates regularly, and at the moment, not all Apex Servers are in that list.

⚠️Warning: Apex Legends doesn't check availability of the servers when queuing for a game, so if your party members don't have the same servers blocked - your party members will get into the match, but you will get disconnected. You don't get a cooldown if that happens.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
  
* Windows 10 or higher (Windows 7/8 is not tested, but might work)
* Python 3.7+

### Installation

1. Get latest Python release [here](https://www.python.org/downloads/). Don't forget to check "Add to PATH" when installing.
2. Clone the repo or download the zip and open cmd in the repo folder
3. Install dependencies for the scripts
   ```sh
   py -3 -m pip install -r requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

⚠️ All script should be run in a cmd with administrator privileges 

1. filter.py - filters Apex Legends servers by ping.
`py -3 filter.py <latency threshold>`  
For example, `py -3 filter.py 200` will write all servers with ping more than 200ms into "high_latency.txt"  
Please note, that running this script could take a few minutes to run, be patient and try not to stress the network too much while it's running.

2. block.py - blocks outgoing connection to IPs in a specified file.  
⚠️Warning: before running block.py, you need to close Apex Legends, for some reason adding firewall rules doesn't work when Apex Legends is running, possibly because of the anticheat.  
`py -3 block.py <IPs file>`  
For example, `py -3 block.py high_latency.txt` will block all servers in file "high_latency.txt"

3. unblock.py - unblocks all IPs that were blocked by "block.py". Takes no arguments.  
`py -3 unblock.py`

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Pavel Levchuk - lev4ukpavel2@gmail.com

Project Link: [https://github.com/16x16/apex-blocker](https://github.com/16x16/apex-blocker)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/16x16/apex-blocker.svg?style=for-the-badge
[contributors-url]: https://github.com/16x16/apex-blocker/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/16x16/apex-blocker.svg?style=for-the-badge
[forks-url]: https://github.com/16x16/apex-blocker/network/members
[stars-shield]: https://img.shields.io/github/stars/16x16/apex-blocker.svg?style=for-the-badge
[stars-url]: https://github.com/16x16/apex-blocker/stargazers
[issues-shield]: https://img.shields.io/github/issues/16x16/apex-blocker.svg?style=for-the-badge
[issues-url]: https://github.com/16x16/apex-blocker/issues
[license-shield]: https://img.shields.io/github/license/16x16/apex-blocker.svg?style=for-the-badge
[license-url]: https://github.com/16x16/apex-blocker/blob/master/LICENSE.txt
