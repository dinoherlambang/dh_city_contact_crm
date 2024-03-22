# Odoo Custom City Module

This module adds a custom city model to Odoo and links it to the `res.partner` and `crm.lead` models. It also includes a state model that is linked to the cities.

## Features

- Adds a new city model with a name field.
- Adds a new state model with a name and code field.
- Modifies the `res.partner` and `crm.lead` models to include a city field.
- Includes an `onchange` method that updates the state field whenever the city field is changed.

## Installation

1. Add this module to your Odoo addons path.
2. Update the module list in the Odoo Apps menu.
3. Install this module from the Odoo Apps menu.

## Usage

After installing the module, you can select a city for any partner or lead. The state field will be automatically updated to match the state of the selected city.

## Module Information

- Author: Dino Herlambang
- Website: Instagram
- Version: 13.0
- Dependencies: `base`, `crm`
- Data Files: `views/views.xml`, `views/templates.xml`, `data/res.kabupaten.csv`, `data/res.country.state.csv`

## Contributing

Contributions are welcome! Please read the contributing guide for details on how to contribute.

## License

This project is licensed under the GNU GPL License - see the LICENSE.md file for details.
