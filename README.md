# WhatsApp Spammer

<p align="center">
  <img src="https://example.com/logo.png" alt="Logo" width="150">
</p>

<p align="center">
  This is a Python script for automating the process of sending multiple messages to a contact on WhatsApp Web.
  The script uses Selenium WebDriver to interact with WhatsApp Web and send spam messages to a specified contact.
</p>

## Features

<ul>
  <li>Automate sending multiple messages to a WhatsApp contact</li>
  <li>Search for contacts using phone numbers</li>
  <li>Configurable number of messages to send</li>
  <li>Delay of 0.1 seconds between messages for rapid spamming</li>
  <li>Uses Selenium WebDriver for browser automation</li>
</ul>

## Requirements

<ul>
  <li>Python 3.x</li>
  <li>Google Chrome browser</li>
  <li>ChromeDriver</li>
  <li>Required Python libraries: <code>selenium</code>, <code>webdriver-manager</code></li>
</ul>

## Installation

<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/yourusername/whatsapp-spammer.git
cd whatsapp-spammer</code></pre>
  </li>
  <li>Install the required Python libraries:
    <pre><code>pip install selenium webdriver-manager</code></pre>
  </li>
  <li>Download and install <a href="https://www.google.com/chrome/">Google Chrome</a>.</li>
  <li>Ensure ChromeDriver is installed and accessible in your PATH. You can install it using the <code>webdriver-manager</code> as shown in the script.</li>
</ol>

## Usage

<ol>
  <li>Open a terminal and navigate to the project directory:
    <pre><code>cd whatsapp-spammer</code></pre>
  </li>
  <li>Run the script:
    <pre><code>python main.py</code></pre>
  </li>
  <li>Follow the prompts:
    <ul>
      <li>Log in to WhatsApp Web using your browser.</li>
      <li>Enter the phone number of the contact you want to spam.</li>
      <li>Enter the message you want to send.</li>
      <li>Specify the number of times you want to send the message.</li>
      <li>Confirm to initiate spamming by entering <code>y</code>.</li>
    </ul>
  </li>
  <li>To exit the script, follow the prompts after the spamming process is complete.</li>
</ol>

## Disclaimer

<p>This script is intended for educational purposes only. Misuse of this tool to harass or spam individuals is strictly prohibited and could result in consequences as per WhatsApp's terms of service. Use this tool responsibly and with consent from the recipient.</p>

## Contributing

<p>Contributions are welcome! If you have suggestions for improvements or new features, feel free to submit a pull request or open an issue.</p>

## License

<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

## Acknowledgements

<ul>
  <li><a href="https://www.selenium.dev/">Selenium</a> for browser automation</li>
  <li><a href="https://github.com/SergeyPirogov/webdriver_manager">WebDriver Manager</a> for managing WebDriver binaries</li>
</ul>

<hr>

<p align="center">Feel free to reach out if you have any questions or need further assistance!</p>
