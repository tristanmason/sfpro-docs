# Search and Filter Documentation

This is a combined documentation file for the Search and Filter WordPress plugin.

---

## Documentation – Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/advanced-custom-fields/

Looking for an
integration
? Checkout the
integrations documentation
below.
Getting Started
Get to grips with basics and build your first search form.
Overview
Installation
Create a Query
Create a Field
Building a Layout
Queries
Find out what Queries are and how you can leverage them to build listings.
Queries Overview
Query Editor
Live Search (Pro)
Results Shortcode (Pro)
Archives
Fields
Learn about the different fields types and how to set them up.
Fields Overview
Field Editor
Field Types
Styles Presets
Learn how to create your own styles presets.
Styles Overview
Styles Editor
FAQ
Some of our most commonly asked questions.
What’s new in version 3?
Can I use my license on local or staging sites?
Debugging
Upgrading to Pro version 3 (from v2)
Troubleshooting
Block Editor
Learn how to create your fields & queries directly in the Block Editor.
Block Editor Overview
Block Editor – Add Fields
Block Editor – Create Queries
Developer
Documentation for advanced integrations & APIs.
Queries
Fields
Theme Integration
Custom query integration
Changelogs
Known Issues
Known issues with third party software and how to work around them.
WP Engine
WP Rocket
Integrations
Integrations
Find out the best way to get up and running using your favorite tools.
Elementor
Beaver Builder
Relevanssi
WPML
GenerateBlocks
Polylang
Dynamic Content for Elementor
Easy Digital Downloads
Divi
WPBakery Page Builder
WooCommerce
Get up an running with WooCommerce, however you use it.
WooCommerce Overview
WooCommerce Shop
WooCommerce Collections Block
Advanced Custom Fields
Learn how to power up your Search & Filter fields with ACF data.
Advanced Custom Fields Overview
Looking for version 2 documentation? Head to the
version 2 documentation site
.
Advanced Custom Fields Overview
Advanced Custom Fields
Read more ->
: Advanced Custom Fields Overview
September 30, 2024

---

## Upgrading to Pro version 3 (from v2) - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/faqs/upgrading-to-pro-v3-from-v2/

This is a guide on how to upgrade from version 2 to version 3.
Notice
– we have extended our end of life dates while we prepare the migration tool.
Version 2 will
continue to be supported
until at least
December 2025
, there is no immediate requirement to upgrade to version 3.
Upgrading from version 2 to version 3 is currently a manual process,
automatic updates are not enabled
for this update.
We are creating a migration tool to help automate this process which will be ready around October 2025.
Checkout the video for an in depth look at how to migrate your site today or take a look below for an overview of the main changes.
Splitting Search Forms
A version 2 search form typically comprises of a
Settings & Defaults
section where you can configure your query and a
Search Form
section for building your search form layout.
Version 3 splits a traditional search form into 2 distinct parts:
Settings & Defaults
are now known as
Queries
Fields
are now split out into their own section and can be reassigned to any
Query
you have created.
Fields
can now be placed individually, anywhere on page, rather than together as a predefined search form.
Queries
Version 3 queries still have many similarities to the
Settings & Defaults
section in version 2.
One of the key differences is that the
display results
tab has been moved to the front and is now called
integration
.
Instead of defining your query settings first, you first choose how to integrate.
Integration methods
One of the biggest changes is the way we setup queries and integrate them in your site. Let’s cover the main differences with each display method.
Post type archive + taxonomy archive
Choosing the post type archive display method allows you to perform searches on your frontend post type archives.
The new way to configure this is to choose your
archive
type from within the
integration
tab, and then your post type.
New to version 3 is support for filtering only on specific taxonomy archives.
Results shortcode
To support displaying the results as a shortcode we need ensure the shortcode option is enabled in our settings screen:
Then enable it in the query settings:
Using the shortcode
Search & Filter shortcodes have changes since version 2, displaying the results should now use the format:
[searchandfilter query="1" action="show-results"]
Note
: the container CSS class has changed to
.search-filter-query--id-1
from
.search-filter-results-1
* The above examples all use
1
as the query ID, be sure to replace this with your actual query ID.
Note:
if you are using an existing results template file from v2, you will also need to add
wp_reset_postdata();
after the
while
loop.
This is standard practice after using functions like
the_post()
, while v2 did this automatically, it also did this in places it wasn’t needed – so now this is a required manual addition.
As an archive (deprecated)
Version 2’s “as an archive” method is no longer available in version 3. The reason being is that it was bad for SEO, and hard to update the page title.
While it allowed you to use custom templates for displaying results in a similar format to post type archives, these archives were never recognised as “true” WordPress archives which meant that SEO plugins also didn’t know what to do with them.
The main advantage of this display method was that you could design your page & results in PHP.
You can still do this today, our recommendation is to use the
shortcode display method
, which allows for PHP customisation of the results.
If it is required to build the entire page in PHP, this can be also already be done in WordPress using
custom page templates
and combining that with our results shortcode to have full control over the page layout.
Integrations
Version 3 supports some of the integrations that were possible in version 2 but not all of them, just yet. We’re working on filling in the missing integrations over the coming months.
Available today
Advanced Custom Fields (ACF)
WooCommerce
Elementor
Beaver Builder
Relevanssi
Currently working on
Dynamic Content for Elementor
Divi
WP Bakery Page Builder
Easy Digital Downloads
New integrations planned
Bricks Builder
Fields
Fields are a lot more flexible in version 3. There are more configuration options, new
design options
, and you can now
move fields from one query to another
.
You can create a field first, then assign it to a query, or add a new field directly to an existing query.
Once you’ve chosen to create a field, you will find the
new field editor
.
Version 3 no longer restricts you to building a singular search form with all your fields in a specific order, you can now
place fields individually
in
any order
and
anywhere
on a page.
Fields can be added using shortcodes (found underneath the field editor) or by using blocks.
Our plan for upgrading
We’ll create a migration tool to convert existing v2 search forms into v3 fields and queries.
After the migration you will need to relink / replace the search forms on the frontend with the new fields
For heavily customised implementations, we’ll release a developer guide on how to migrate – this will be a manual process and will require some development time.
On This Page
Splitting Search Forms
Queries
Integration methods
As an archive (deprecated)
Integrations
Fields
Our plan for upgrading
More From This Series
FAQs
What’s new in version 3?
Can I use my license on local or staging sites?
Debugging
Upgrading to Pro version 3 (from v2)
Troubleshooting

---

## Documentation – Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/fields/

Looking for an
integration
? Checkout the
integrations documentation
below.
Getting Started
Get to grips with basics and build your first search form.
Overview
Installation
Create a Query
Create a Field
Building a Layout
Queries
Find out what Queries are and how you can leverage them to build listings.
Queries Overview
Query Editor
Live Search (Pro)
Results Shortcode (Pro)
Archives
Fields
Learn about the different fields types and how to set them up.
Fields Overview
Field Editor
Field Types
Styles Presets
Learn how to create your own styles presets.
Styles Overview
Styles Editor
FAQ
Some of our most commonly asked questions.
What’s new in version 3?
Can I use my license on local or staging sites?
Debugging
Upgrading to Pro version 3 (from v2)
Troubleshooting
Block Editor
Learn how to create your fields & queries directly in the Block Editor.
Block Editor Overview
Block Editor – Add Fields
Block Editor – Create Queries
Developer
Documentation for advanced integrations & APIs.
Queries
Fields
Theme Integration
Custom query integration
Changelogs
Known Issues
Known issues with third party software and how to work around them.
WP Engine
WP Rocket
Integrations
Integrations
Find out the best way to get up and running using your favorite tools.
Elementor
Beaver Builder
Relevanssi
GenerateBlocks
WPML
Polylang
Dynamic Content for Elementor
Divi
WPBakery Page Builder
Easy Digital Downloads
WooCommerce
Get up an running with WooCommerce, however you use it.
WooCommerce Overview
WooCommerce Shop
WooCommerce Collections Block
Advanced Custom Fields
Learn how to power up your Search & Filter fields with ACF data.
Advanced Custom Fields Overview
Looking for version 2 documentation? Head to the
version 2 documentation site
.
Fields Overview
Fields
Fields allow your visitors to interact with queries on your site, enabling them to drill down to find the information they are looking for. This means they spend less time looking for the information they need. Field types There are 5 different types of fields: Search, Choice, Range (pro), Advanced and Control. Search fields allow…
Read more ->
: Fields Overview
September 4, 2022
Field Editor
Fields
The field editor allows you to create, edit and design the frontend fields on your site. Access the field editor via the Search & Filter Dashboard, then choose Fields in the main menu. If you are using the block editor, you can access all the same settings and features directly via our block equivalents. Name…
Read more ->
: Field Editor
December 17, 2023
Field Types
Fields
There are 5 different types of fields: Search, Choice, Range, Advanced and Control. Search Fields Search fields allow for free text input to search for posts matching the search term. Input types include: Choice Fields Choice fields allow for a single selection or multiple selection from a set of options. Input types include: Coming soon:…
Read more ->
: Field Types
September 5, 2022

---

## Documentation – Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/woocommerce/

Looking for an
integration
? Checkout the
integrations documentation
below.
Getting Started
Get to grips with basics and build your first search form.
Overview
Installation
Create a Query
Create a Field
Building a Layout
Queries
Find out what Queries are and how you can leverage them to build listings.
Queries Overview
Query Editor
Live Search (Pro)
Results Shortcode (Pro)
Archives
Fields
Learn about the different fields types and how to set them up.
Fields Overview
Field Editor
Field Types
Styles Presets
Learn how to create your own styles presets.
Styles Overview
Styles Editor
FAQ
Some of our most commonly asked questions.
What’s new in version 3?
Can I use my license on local or staging sites?
Debugging
Upgrading to Pro version 3 (from v2)
Troubleshooting
Block Editor
Learn how to create your fields & queries directly in the Block Editor.
Block Editor Overview
Block Editor – Add Fields
Block Editor – Create Queries
Developer
Documentation for advanced integrations & APIs.
Queries
Fields
Theme Integration
Custom query integration
Changelogs
Known Issues
Known issues with third party software and how to work around them.
WP Engine
WP Rocket
Integrations
Integrations
Find out the best way to get up and running using your favorite tools.
Elementor
Beaver Builder
Relevanssi
WPML
GenerateBlocks
Polylang
Dynamic Content for Elementor
Easy Digital Downloads
Divi
WPBakery Page Builder
WooCommerce
Get up an running with WooCommerce, however you use it.
WooCommerce Overview
WooCommerce Shop
WooCommerce Collections Block
Advanced Custom Fields
Learn how to power up your Search & Filter fields with ACF data.
Advanced Custom Fields Overview
Looking for version 2 documentation? Head to the
version 2 documentation site
.
WooCommerce Overview
WooCommerce
Search & Filter has a deep integration with WooCommerce built in, all you need to do is enable it! Enable the Integration Head to wp-admin -> Search & Filter -> Integrations and ensure the WooCommerce integration is enabled. WooCommerce Shop Search & Filter supports both FSE and classic editor Shop pages. To add filtering to…
Read more ->
: WooCommerce Overview
October 7, 2024
WooCommerce Shop
WooCommerce
The first step is to ensure our WooCommerce integration is enabled. Enable the Integration Head to wp-admin -> Search & Filter -> Integrations and ensure the WooCommerce integration is enabled. Create a Query To link our fields with the WooCommerce Shop query, we need to create a query integration. Head to wp-admin -> Search &…
Read more ->
: WooCommerce Shop
September 20, 2024
WooCommerce Collections Block
WooCommerce
The first step is to ensure our WooCommerce integration is enabled. Enable the Integration Head to wp-admin -> Search & Filter -> Integrations and ensure the WooCommerce integration is enabled. Create a Page with the Collections Block Add a Product Collection block from the Block Inserter and then choose Create Your Own: To link our…
Read more ->
: WooCommerce Collections Block
March 17, 2025

---

## Relevanssi - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/integrations/relevanssi/

Relevanssi allows you to perform text searches inside posts, custom fields, tags, categories, taxonomy terms and more. It provides advanced ordering features such as ordering by weight parameters.
Enabling Relevanssi integration with Search & Filter means our search fields will be affected by your Relevanssi settings and also have the benefits of the Relevanssi indexer to keep complex keyword searches quick.
Our Relevanssi integration is a pro feature.
How to use
Goto the Search & Filter Integrations Dashboard
First make sure the Relevanssi plugin is enabled, and then head to our integrations page.
Enable the Relevanssi Integration
Enable the Relevanssi Integration.
Now you can connect your search fields to Relevanssi.
Connect Relevanssi to a search field
From any of your search fields, select the
data type
dropown and choose
Relevanssi
as the source.
And that’s it, you’re ready to go!
On This Page
How to use
Goto the Search & Filter Integrations Dashboard
Enable the Relevanssi Integration
Connect Relevanssi to a search field
More From This Series
Integrations
Elementor
Beaver Builder
Relevanssi
GenerateBlocks
WPML
Polylang
Dynamic Content for Elementor
Easy Digital Downloads
Divi
WPBakery Page Builder

---

## Polylang - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/integrations/polylang/

The Polylang integration is not quite ready for Search & Filter Version 3 – but we’re working on it!
Checkout the version 2 documentation here.
More From This Series
Integrations
Elementor
Beaver Builder
Relevanssi
GenerateBlocks
WPML
Polylang
Dynamic Content for Elementor
Easy Digital Downloads
Divi
WPBakery Page Builder

---

## Styles Overview - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/styles/styles-overview/

*
Styling of fields has changed significantly. This section is being updated.
The styles section allow you to define a styles preset to apply to your fields.
For now this is limited to color choices only, in future this will incorperate fonts, borders, spacing, and possibly more.
Creating custom styles
Head to the
styles
tab in the
Search & Filter dashboard
.
Select
Add New
This brings up the styles editor, where you can begin changing the styles attributes.
Default styles
Default styles allow you to quickly and easily swap fields connected to the defaults styles, with another styles preset.
Lets imagine you have a 3 fields on your site, all set to use
default styles
.
After designing a new styles preset, you can set it to be the default, and the appearance of all 3 fields will update instantly across your site.
To set your styles as default, use the 3 dot icon and choose “Set as default”.
Dropdown menu for the styles preset
Once a styles preset is set as default, it cannot be disabled, deleted or trashed.
Applying styles to fields
When fields are created, they are assigned to the default styles prest.
To change to any other styles preset, choose a styles preset from the dropdown option. This is available to all fields.
On This Page
Creating custom styles
Default styles
Applying styles to fields
More From This Series
Styles
Styles Overview
Styles Editor

---

## Troubleshooting - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/faqs/troubleshooting/

Checking for conflicts
One of the first steps when troubleshooting is checking for conflicts with plugins and themes.
The WordPress ecosystem is vast, and there is no reliable way to ensure that a specific plugin will work well with another, or a specific theme.
By using the WordPress APIs and coding standards, we can improve compatibility, but its not a guarantee.
Download the Health Check Plugin
WordPress comes with the a
site health check
built in since version 5.2, however the official site health check plugin comes with additional tools.
The
troubleshooting tools
allow us to disable plugins and themes temporarily without affecting visitors to your site.
You can
download it from the official repo here
.
Enable Troubleshooting mode
Once installed, you can head to
Tools
->
Site Health
->
Troubleshooting
Then press the
Enable Troubleshooting Mode
button.
Enable the Search & Filter plugins
Once troubleshooting mode is enabled, you’ll notice that everything is disabled, including plugins and theme.
This won’t affect visitors to your site, this is only visible to you while you are logged in to your account.
Re-enable our plugins and any other other plugins our plugin needs (like post types and taxonomy related plugins)
Testing the issue again
Now we’ve ruled out other plugins and themes as a potential conflict, we can retest to see if the problem still exists.
Possible outcomes:
If the issue is still there, then there could be a bug, please open a support ticket for us to investigate.
If the issue has gone, then we can find the source of the issue be re-enabling plugins and themes one by one, until we see the issue re-occur. Once you know which plugin or theme it is, let us know so we can also investigate.
On This Page
Checking for conflicts
Download the Health Check Plugin
Enable Troubleshooting mode
Enable the Search & Filter plugins
Testing the issue again
More From This Series
FAQs
What’s new in version 3?
Can I use my license on local or staging sites?
Debugging
Upgrading to Pro version 3 (from v2)
Troubleshooting

---

## Documentation – Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/developer/?query-0-page=2

Looking for an
integration
? Checkout the
integrations documentation
below.
Getting Started
Get to grips with basics and build your first search form.
Queries
Find out what Queries are and how you can leverage them to build listings.
Fields
Learn about the different fields types and how to set them up.
Styles Presets
Learn how to create your own styles presets.
FAQ
Some of our most commonly asked questions.
Block Editor
Learn how to create your fields & queries directly in the Block Editor.
Developer
Documentation for advanced integrations & APIs.
Known Issues
Known issues with third party software and how to work around them.
Integrations
Integrations
Find out the best way to get up and running using your favorite tools.
WooCommerce
Get up an running with WooCommerce, however you use it.
Advanced Custom Fields
Learn how to power up your Search & Filter fields with ACF data.
Looking for version 2 documentation? Head to the
version 2 documentation site
.
Changelogs
Developer
Below are the changelogs for the Search & Filter plugins and their extensions.
Read more ->
: Changelogs
January 11, 2025

---

## Documentation – Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/integrations/

Looking for an
integration
? Checkout the
integrations documentation
below.
Getting Started
Get to grips with basics and build your first search form.
Overview
Installation
Create a Query
Create a Field
Building a Layout
Queries
Find out what Queries are and how you can leverage them to build listings.
Queries Overview
Query Editor
Live Search (Pro)
Results Shortcode (Pro)
Archives
Fields
Learn about the different fields types and how to set them up.
Fields Overview
Field Editor
Field Types
Styles Presets
Learn how to create your own styles presets.
Styles Overview
Styles Editor
FAQ
Some of our most commonly asked questions.
What’s new in version 3?
Can I use my license on local or staging sites?
Debugging
Upgrading to Pro version 3 (from v2)
Troubleshooting
Block Editor
Learn how to create your fields & queries directly in the Block Editor.
Block Editor Overview
Block Editor – Add Fields
Block Editor – Create Queries
Developer
Documentation for advanced integrations & APIs.
Queries
Fields
Theme Integration
Custom query integration
Changelogs
Known Issues
Known issues with third party software and how to work around them.
WP Engine
WP Rocket
Integrations
Integrations
Find out the best way to get up and running using your favorite tools.
Elementor
Beaver Builder
Relevanssi
WPML
GenerateBlocks
Polylang
Dynamic Content for Elementor
Easy Digital Downloads
Divi
WPBakery Page Builder
WooCommerce
Get up an running with WooCommerce, however you use it.
WooCommerce Overview
WooCommerce Shop
WooCommerce Collections Block
Advanced Custom Fields
Learn how to power up your Search & Filter fields with ACF data.
Advanced Custom Fields Overview
Looking for version 2 documentation? Head to the
version 2 documentation site
.
Advanced Custom Fields Overview
Advanced Custom Fields
Read more ->
: Advanced Custom Fields Overview
September 30, 2024
WooCommerce Overview
WooCommerce
Search & Filter has a deep integration with WooCommerce built in, all you need to do is enable it! Enable the Integration Head to wp-admin -> Search & Filter -> Integrations and ensure the WooCommerce integration is enabled. WooCommerce Shop Search & Filter supports both FSE and classic editor Shop pages. To add filtering to…
Read more ->
: WooCommerce Overview
October 7, 2024
WooCommerce Shop
WooCommerce
The first step is to ensure our WooCommerce integration is enabled. Enable the Integration Head to wp-admin -> Search & Filter -> Integrations and ensure the WooCommerce integration is enabled. Create a Query To link our fields with the WooCommerce Shop query, we need to create a query integration. Head to wp-admin -> Search &…
Read more ->
: WooCommerce Shop
September 20, 2024
Elementor
Integrations
The Search & Filter – Elementor Extension allows for seamless integration between Elementor and Search & Filter. With this extension, Search & Filter will now be able to directly integrate and filter the following Elementor widgets: Install + activate the extension To get started first we need to enable the integration in our integrations screen.…
Read more ->
: Elementor
September 30, 2024
WooCommerce Collections Block
WooCommerce
The first step is to ensure our WooCommerce integration is enabled. Enable the Integration Head to wp-admin -> Search & Filter -> Integrations and ensure the WooCommerce integration is enabled. Create a Page with the Collections Block Add a Product Collection block from the Block Inserter and then choose Create Your Own: To link our…
Read more ->
: WooCommerce Collections Block
March 17, 2025
Beaver Builder
Integrations
The Search & Filter – Beaver Builder Extension allows for seamless integration between Beaver Builder and Search & Filter. With this extension, Search & Filter will now be able to directly integrate and filter the following Beaver Builder Modules: This includes support for Beaver Themer and archive locations. Install + activate the extension To get…
Read more ->
: Beaver Builder
September 30, 2024
Relevanssi
Integrations
Relevanssi allows you to perform text searches inside posts, custom fields, tags, categories, taxonomy terms and more. It provides advanced ordering features such as ordering by weight parameters. Enabling Relevanssi integration with Search & Filter means our search fields will be affected by your Relevanssi settings and also have the benefits of the Relevanssi indexer…
Read more ->
: Relevanssi
September 30, 2024
WPML
Integrations
Both Search & Filter Pro and the Base (free) version integrate with WPML via our Search & Filter – WPML Extension plugin – allowing you translate your search & filter fields and search for content in any language! Get the Extension Via the Pro Plugin Enable the extension by heading to wp-admin -> Search &…
Read more ->
: WPML
September 30, 2024
GenerateBlocks
Integrations
The Search & Filter – GenerateBlocks Extension allows for seamless integration between GenerateBlocks 2 and Search & Filter. With this extension, Search & Filter will now be able to directly integrate and filter the GenerateBlocks Query block. This includes support for Full Site Editing and archive locations. Install + activate the extension To get started…
Read more ->
: GenerateBlocks
February 19, 2025
Polylang
Integrations
The Polylang integration is not quite ready for Search & Filter Version 3 – but we’re working on it! Checkout the version 2 documentation here.
Read more ->
: Polylang
September 30, 2024

---

## WooCommerce Shop - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/woocommerce/woocommerce-shop/

The first step is to ensure our WooCommerce integration is enabled.
Enable the Integration
Head to
wp-admin
->
Search & Filter
->
Integrations
and ensure the WooCommerce integration is enabled.
Create a Query
To link our fields with the WooCommerce Shop query, we need to create a query integration.
Head to
wp-admin
->
Search & Filter
->
Queries
->
Add New
to create a query.
Ensure
Location
is set to
WooCommerce Shop
.
Add Fields with the Block Editor + FSE
If you’re using a block editor theme with FSE enabled, the way to modify your shop page is via the site editor.
Head to your shop page and find the
Edit Site
link in the admin bar:
Add Blocks – Search, Choice, Range & Control
Use our Search, Choice, Range and Control field blocks to build your layout and search form:
Ensure the Fields you create are set to use the WooCommerce Shop query you created earlier, this can be found in the inspector panel:
Add Fields – Classic Themes / Admin UI
If you’re not using the block editor you might be able to use one of our page builder integrations, or you can build your fields directly in our admin UI and add them later to your pages.
After you’ve created your query in our admin dashboard, you can create fields directly below:
Once you’ve created a field, you can use it’s shortcode (found underneath the field editor) to place them anywhere on your site:
Adding Fields to your Shop Page
Depending on your theme you might be able to add fields to your sidebars via the widget editor, or you can edit your shop page directly.
Head to
wp-admin
->
Pages
->
Shop Page
Add your Field Shortcodes:
On This Page
Enable the Integration
Create a Query
Add Fields with the Block Editor + FSE
Add Blocks – Search, Choice, Range & Control
Add Fields – Classic Themes / Admin UI
Adding Fields to your Shop Page
More From This Series
WooCommerce
WooCommerce Overview
WooCommerce Shop
WooCommerce Collections Block

---

## Easy Digital Downloads - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/integrations/easy-digital-downloads/

The Easy Digital Downloads integration is not quite ready for Search & Filter Version 3 – but we’re working on it!
Checkout the version 2 documentation here.
More From This Series
Integrations
Elementor
Beaver Builder
Relevanssi
GenerateBlocks
WPML
Polylang
Dynamic Content for Elementor
Easy Digital Downloads
Divi
WPBakery Page Builder

---

## Overview - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/getting-started/overview/

Installation
If you are familiar with WordPress, login to your site and search/install the Search & Filter plugin from the plugins page
(once we’re out of beta)
.
For more details, you can
read our step by step installation instructions
.
The basics
There are two main concepts that drive this plugin:
Queries
Fields
Queries
Queries are the backbone of your site. They are used for generating lists of items and they can be found in many different places; you’ll no doubt have come across them already. Some examples are:
Search results
Blog listings
Post lists and grids
Product lists and grids
Galleries
Tag and Category archives
Custom Post Type archives
And there are many more…
The query section of this plugin can be used to modify and create different queries on your site, changing options such as post types, order of results, posts per page as well as other settings.
Learn how to Create a Query
Fields
Fields are form fields your visitors will see on your site, such as a search box, dropdown or submit button.
With Search & Filter, you can create fields and add them to your site – visitors will be able use them to refine a query to help them easily find what they are looking for.
Learn how to Create a Field
On This Page
Installation
The basics
Queries
Fields
More From This Series
Getting Started
Overview
Installation
Create a Query
Create a Field
Building a Layout

---

## Documentation – Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/developer/

Looking for an
integration
? Checkout the
integrations documentation
below.
Getting Started
Get to grips with basics and build your first search form.
Overview
Installation
Create a Query
Create a Field
Building a Layout
Queries
Find out what Queries are and how you can leverage them to build listings.
Queries Overview
Query Editor
Live Search (Pro)
Results Shortcode (Pro)
Archives
Fields
Learn about the different fields types and how to set them up.
Fields Overview
Field Editor
Field Types
Styles Presets
Learn how to create your own styles presets.
Styles Overview
Styles Editor
FAQ
Some of our most commonly asked questions.
What’s new in version 3?
Can I use my license on local or staging sites?
Debugging
Upgrading to Pro version 3 (from v2)
Troubleshooting
Block Editor
Learn how to create your fields & queries directly in the Block Editor.
Block Editor Overview
Block Editor – Add Fields
Block Editor – Create Queries
Developer
Documentation for advanced integrations & APIs.
Queries
Fields
Theme Integration
Custom query integration
Changelogs
Known Issues
Known issues with third party software and how to work around them.
WP Engine
WP Rocket
Integrations
Integrations
Find out the best way to get up and running using your favorite tools.
Elementor
Beaver Builder
Relevanssi
WPML
GenerateBlocks
Polylang
Dynamic Content for Elementor
Easy Digital Downloads
Divi
WPBakery Page Builder
WooCommerce
Get up an running with WooCommerce, however you use it.
WooCommerce Overview
WooCommerce Shop
WooCommerce Collections Block
Advanced Custom Fields
Learn how to power up your Search & Filter fields with ACF data.
Advanced Custom Fields Overview
Looking for version 2 documentation? Head to the
version 2 documentation site
.
GenerateBlocks Extension
Developer
Read more ->
: GenerateBlocks Extension
June 1, 2025
Queries
Developer
PHP Filter query args The query class: Search_Filter\Queries\Query The query instance class. Function: get_attributes() Description: Gets all the attributes for a query (most of the settings you can see in the query editor).Return: associative array of attributes.Use: $query->get_attributes() Function: get_attribute( $attribute_name ) Description: Gets a single attribute by name.Return: attribute value or null if attribute…
Read more ->
: Queries
September 27, 2024
Search & Filter
Developer
Read more ->
: Search & Filter
January 11, 2025
Search & Filter Pro
Developer
Read more ->
: Search & Filter Pro
January 11, 2025
Fields
Developer
PHP The field class: Search_Filter\Fields\Field The field instance class. Function: get_attributes() Description: Gets all the attributes for a query (most of the settings you can see in the query editor).Return: associative array of attributes.Use: $query->get_attributes() Function: get_attribute( $attribute_name ) Description: Gets a single attribute by name.Return: attribute value or null if attribute not found.Use: $query->get_attribute(‘singleIntegration’)…
Read more ->
: Fields
November 26, 2024
Elementor Extension
Developer
Read more ->
: Elementor Extension
January 11, 2025
Beaver Builder Extension
Developer
Read more ->
: Beaver Builder Extension
January 11, 2025
WPML Extension
Developer
Read more ->
: WPML Extension
January 11, 2025
Theme Integration
Developer
Search & Filter supports integration with themes by allowing them define a set of styles to use. This allows theme builders to provide a seamless integration of their theme styling with Search & Filter. How it works If a theme opts in to supporting Search & Filter styles then a “Theme” styles preset will be…
Read more ->
: Theme Integration
July 5, 2023
Custom query integration
Developer
Creating a custom query integration requries several steps depending on your needs. Setting up your query To connect Search & Filter with your query you will need to add an argument to the query itself with the name search_filter_query_id. The value of this argument should be the ID of of the Search & Filter query…
Read more ->
: Custom query integration
September 29, 2023

---

## Block Editor - Create Queries - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/block-editor/block-editor-create-queries/

Creating Search & Filter Queries
How it Works
Search & Filter comes with its own advanced query editor – acting as a bridge between results listings and our fields.
To connect a field to a query, we need to:
Create a Search & Filter Query
Assign Fields to the Query
Assign the Search & Filter Query to results/listing (most likely the Query Loop block)
Creating Queries
While it is possible to create queries & fields via our admin pages, everything is also available directly in the block editor – which means you never need to interrupt your workflow to build queries & fields with Search & Filter.
If you’ve already added a field to the block editor, you can select the
Add Query
or
Edit Query
options from the
Query Integration Panel
.
Query Editor Modal
Adding or editing a query will open the query editor modal.
The main settings to configure to connect to a Query Loop Block are:
Location
– set this to
Dynamic
to use the current page, but you might want to set this to
Single
and specify a page if your results are on another page, or
Archive
if you’re using FSE and want to filter archives.
Query
– Set this to
Query Loop Block
to integrate with WordPress’ built in Query Loop Block. Choose another query type if you need to connect with a different type of query.
Autodetect Query
– Enable this option to autodetect which Query Loop Block to connect with. If you are using more than one query loop block, its recommended not to use autodetection and instead specify the query connect to
via the Query Loop Block dropdown
.
There are a lot of configuration options for Search & Filter Queries, such as the ability to create post meta and taxonomy queries, add multiple levels of sorting, include/exclude posts and pages, and much more.
Learn More about Search & Filter Queries
Live Search & Loading Icon (Pro)
It is generally recommended to enable
Live Search
via the Live Search tab, which then reveals further customisation options such as the
loading icon
.
Query Loop Block
One of the Block Editors most powerful tools is the Query Loop Block.
This block allows you to create listing and grids of your posts, and granularly control the layout and design of each item in the listing.
Choose a preset or create your own designs to create rich post listings.
Connect To a Search & Filter Query
Once you’ve created your design and layout, you can then connect a Query Loop Block to a Search & Filter Query.
Option 1: Auto-detect the Query Loop
In your query settings ensure that auto-detect is enabled and Search & Filter will detect any query loops on the same page where you have placed your filters.
Option 2: The Query Dropdown
Search & Filter adds a new Query Selection dropdown to the Query Loop inspector. Choose your desired query from the dropdown or start typing to search by name.
Query Block Variations
Many plugins extend the query loop block and create their own variations. Our Auto-detect feature won’t work with those, but you can use the
Search & Filter Query
dropdown (pictured above) to connect them to a query.
On This Page
Creating Search & Filter Queries
How it Works
Creating Queries
Query Editor Modal
Live Search & Loading Icon (Pro)
Query Loop Block
Connect To a Search & Filter Query
More From This Series
Block Editor
Block Editor Overview
Block Editor – Add Fields
Block Editor – Create Queries

---

## WooCommerce Collections Block - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/woocommerce/woocommerce-collections-block/

The first step is to ensure our WooCommerce integration is enabled.
Enable the Integration
Head to
wp-admin
->
Search & Filter
->
Integrations
and ensure the WooCommerce integration is enabled.
Create a Page with the Collections Block
Add a
Product Collection
block from the Block Inserter and then choose
Create Your Own
:
To link our fields with the WooCommerce Shop query, we need to create a query integration.
Head to
wp-admin
->
Search & Filter
->
Queries
->
Add New
to create a query.
Ensure
Location
is set to
WooCommerce Shop
.
Add Fields
Via the Block Editor or FSE
If you’re using a block editor theme with FSE enabled, the way to modify your shop page is via the site editor.
Head to your shop page and find the
Edit Site
link in the admin bar:
Search, Choice, Range & Control Blocks
Use our Search, Choice, Range and Control field blocks to build your layout and search form:
Ensure the Fields you create are set to use the WooCommerce Shop query you created earlier, this can be found in the inspector panel:
Via Classic Themes / Admin UI
If you’re not using the block editor you might be able to use one of our page builder integrations, or you can build your fields directly in our admin UI and add them later to your pages.
After you’ve created your query in our admin dashboard, you can create fields directly below:
Once you’ve created a field, you can use it’s shortcode (found underneath the field editor) to place them anywhere on your site:
Adding Fields to your Shop Page
Depending on your theme you might be able to add to your sidebars via the widget editor, or you can edit your shop page.
Head to
wp-admin
->
Pages
–
Shop Page
Add your Field Shortcodes:
On This Page
Enable the Integration
Create a Page with the Collections Block
Add Fields
Via the Block Editor or FSE
Via Classic Themes / Admin UI
More From This Series
WooCommerce
WooCommerce Overview
WooCommerce Shop
WooCommerce Collections Block

---

## Building a Layout - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/getting-started/building-a-layout/

After having created a Search & Filter query and at least one field, you’re now ready to combine them into a search form and results. For this example, we’ll gonna be using a WordPress page, but it is possible to add a search form to any place in your site that you can edit and add a shortcode or a block to.
Note:
Search & Filter Pro integrates with Elementor, Beaver Builder, and more plugins that can further expand the places where you can add and create search forms and results. You can find out more about the supported integrations here.
In order to create a search form with your results, there are three main methods you can use to add a query and the fields you’ve created:
By using Blocks
By using Shortcodes
Via an Integration
We’ll focus on the first two options for this article.
Blocks
Log into your WordPress admin dashboard.
Click on the
Pages > Add New Page
.
You can choose one of the supported patterns for newer WordPress versions or click on the
X
button on the upper left corner of the pop-up if you want to design the entire page manually.
Then, you can either click on the
+
button in the upper left corner or type / and the name of the block you’re trying to add in order to proceed. For this example, we’re gonna start by adding a
Query Loop
block.
Like step 3, you can choose a pattern or design your own manually. For our article, we’ll use a template to proceed. This block will be used to output the results of the search your users will make.
After adding the
Query Loop
block, you’ll need to select it again and then make some changes on the
Block
side menu on the right side. More specifically, you’ll need to change the
Search & Filter Query
setting so that it uses the query we just created.
For this example, we’re gonna use the query titled
My first query
as shown in the example below:
Note:
If you’re having trouble clicking on the
Query Loop
block, you can find a list of all the added blocks of your page by clicking on the three horizontal lines icon on the upper left page as highlighted above. Then, you’ll need to click on the parent block, as shown in the screenshot above, before you can find the
Search & Filter Query.
After this step is done, it’s time to add your fields. Since we’ve already created
Reusable Fields
, we’ll need to use the relevant block so that all our changes persist on this page, too. Click on the
+
icon on the upper left corner of the page.
Then find and add the
Reusable Field
block.
On the right-side menu, you’ll notice a dropdown menu titled
Find Reusable Field
. Click on that and choose the field you want to add. For this example, we’ll use the field we created in the previous step of this guide.
After you select the field you want to add, there are a couple of ways to move it around the page. You can:
Click on the three horizontal lines (like step 6) and drag and drop the element anywhere you’d like in the layout.
Click on the block and then on the arrow up (or down) as highlighted below:
Don’t forget to click on the
Save
button on the upper right corner to save your changes.
And you’re done! You have created your first search form using Search & Filter.
Shortcodes
Log into your WordPress admin dashboard.
Click on the
Pages > Add New Page
.
You can choose one of the supported patterns for newer WordPress versions or click on the
X
button on the upper left corner of the pop-up if you want to design the entire page manually.
Then, you can either click on the
+
button in the upper left corner or type / and the name of the block you’re trying to add in order to proceed. For this example, we’re gonna start by adding a
Shortcode
block.
Note:
For this example, we’re using a theme that supports
Blocks.
However, if your theme doesn’t support that feature, you can add a
Shortcode
using the method that your theme supports.
Now, click on the
Save draft
button on the upper right corner of the page and then return to your site’s WordPress admin dashboard.
Since we already created a query in a previous step of our guide, you can just go to the
Search & Filter > Queries
page and click on the
Edit
button.
In the
Location
tab, you’ll find the
Results Shortcode
field. Click on the
Copy
button.
Then, return to the page you were editing and add the shortcode inside the block:
Now, you’ll need to repeat steps 3 to 5 to add a second shortcode block and then click on the
Save draft
button again.
Return to your site’s WordPress admin dashboard and navigate to the
Search & Filter > Fields
page.
There, click on the three dots as highlighted on the screenshot below and then on the
Copy Shortcode
button.
Once more, return to the page you’re creating and add the shortcode in the second
Shortcode
block as shown below:
Click on the
Publish
button in the upper-right corner if you’re ready to publish the page, or click on the
Save draft
button if you’d like to continue working on it.
Well done! You’ve created your first Search & Filter search form using shortcodes.
Keep in mind that when using shortcodes, each field will use its own shortcode field or block. Click here to continue reading about queries, fields, and more.
On This Page
Blocks
Shortcodes
More From This Series
Getting Started
Overview
Installation
Create a Query
Create a Field
Building a Layout

---

## Advanced Custom Fields Overview - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/guides/advanced-custom-fields-acf/

This article will be back up soon.
More From This Series
Advanced Custom Fields
Advanced Custom Fields Overview

---

## Field Types - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/fields/field-types/

There are 5 different types of fields:
Search
,
Choice
,
Range
,
Advanced
and
Control
.
Search Fields
Search fields allow for free text input to search for posts matching the search term.
Input types include:
Text
– a simple text input that most users will be familiar with.
Autocomplete
(Pro) – start typing to display list of suggestions based on the field data type.
Choice Fields
Choice fields allow for a single selection or multiple selection from a set of options.
Input types include:
Select
(and combobox) – a drop-down displaying possible options, allows for multiple and single selection.
Checkbox
– select one or more options using checkboxes.
Radio
– a radio group where only single selection is possible.
Button
– a button group allowing for single or multiple selection.
Coming soon:
Star rating
– allow filtering for ratings with a more user friendly UI
Color picker
– show options as a color palette.
Range Fields
Range fields are only available in Pro.
Range fields allow users to select a single numerical value within a specified range, or select two values to define a range to filter.
Select
– use drop-downs to select a value.
Radio
– select a single value with a radio group.
Slider
– use a range slider to set values.
Advanced Fields
Advanced fields have more complex functionality than the other field types.
Current there is one input type:
Date picker
– select a single date or date range (ranges are coming soon).
Coming soon:
Maps
(Pro) – show your results on maps!
Control Fields
Control fields interact with the query in different ways, such as submitting a search, resetting the fields, or changing the page of results. They include:
Submit
Reset
Current selection
(Pro)
Sort order
Load more
(Pro)
On This Page
Search Fields
Choice Fields
Range Fields
Advanced Fields
Control Fields
More From This Series
Fields
Fields Overview
Field Editor
Field Types

---

## What's new in version 3? - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/faqs/whats-new-in-version-3/

More From This Series
FAQs
What’s new in version 3?
Can I use my license on local or staging sites?
Debugging
Upgrading to Pro version 3 (from v2)
Troubleshooting

---

## Dynamic Content for Elementor - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/integrations/dynamic-content-for-elementor/

Create a Search & Filter Query (+ Fields)
Head to
wp-admin
->
Search & Filter
->
Queries
->
Add New
to create a query.
Ensure
Location
is set to
Dynamic
and that Query is set to
Dynamic.ooo – Dynamic Content for Elementor
:
Create Fields
Once you’ve created your query, you can add create Fields below to be used later for filtering.
Check the Elementor Documentation
for more information.
Add the Dynamic Posts or Maps widget to a page
From the Elementor Editor, add your
Dynamic Posts
or
Maps
widgets to the page:
Set the Query to your Search & Filter Query
In the Dynamic Posts (or Maps) panel, set the
Query
to use
Search & Filter
then choose your query from the dropdown.
Add Search & Filter fields to your page
Use the
Search & Filter Field
widget to add your fields to your page.
That’s it, you’re good to go!
On This Page
Create a Search & Filter Query (+ Fields)
Create Fields
Add the Dynamic Posts or Maps widget to a page
Set the Query to your Search & Filter Query
More From This Series
Integrations
Elementor
Beaver Builder
Relevanssi
GenerateBlocks
WPML
Polylang
Dynamic Content for Elementor
Easy Digital Downloads
Divi
WPBakery Page Builder

---

## Overview - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/getting-started/

Installation
If you are familiar with WordPress, login to your site and search/install the Search & Filter plugin from the plugins page
(once we’re out of beta)
.
For more details, you can
read our step by step installation instructions
.
The basics
There are two main concepts that drive this plugin:
Queries
Fields
Queries
Queries are the backbone of your site. They are used for generating lists of items and they can be found in many different places; you’ll no doubt have come across them already. Some examples are:
Search results
Blog listings
Post lists and grids
Product lists and grids
Galleries
Tag and Category archives
Custom Post Type archives
And there are many more…
The query section of this plugin can be used to modify and create different queries on your site, changing options such as post types, order of results, posts per page as well as other settings.
Learn how to Create a Query
Fields
Fields are form fields your visitors will see on your site, such as a search box, dropdown or submit button.
With Search & Filter, you can create fields and add them to your site – visitors will be able use them to refine a query to help them easily find what they are looking for.
Learn how to Create a Field
On This Page
Installation
The basics
Queries
Fields
More From This Series
Getting Started
Overview
Installation
Create a Query
Create a Field
Building a Layout

---

## Documentation – Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/queries/

Looking for an
integration
? Checkout the
integrations documentation
below.
Getting Started
Get to grips with basics and build your first search form.
Overview
Installation
Create a Query
Create a Field
Building a Layout
Queries
Find out what Queries are and how you can leverage them to build listings.
Queries Overview
Query Editor
Live Search (Pro)
Results Shortcode (Pro)
Archives
Fields
Learn about the different fields types and how to set them up.
Fields Overview
Field Editor
Field Types
Styles Presets
Learn how to create your own styles presets.
Styles Overview
Styles Editor
FAQ
Some of our most commonly asked questions.
What’s new in version 3?
Can I use my license on local or staging sites?
Debugging
Upgrading to Pro version 3 (from v2)
Troubleshooting
Block Editor
Learn how to create your fields & queries directly in the Block Editor.
Block Editor Overview
Block Editor – Add Fields
Block Editor – Create Queries
Developer
Documentation for advanced integrations & APIs.
Queries
Fields
Theme Integration
Custom query integration
Changelogs
Known Issues
Known issues with third party software and how to work around them.
WP Engine
WP Rocket
Integrations
Integrations
Find out the best way to get up and running using your favorite tools.
Elementor
Beaver Builder
Relevanssi
GenerateBlocks
WPML
Polylang
Dynamic Content for Elementor
Divi
WPBakery Page Builder
Easy Digital Downloads
WooCommerce
Get up an running with WooCommerce, however you use it.
WooCommerce Overview
WooCommerce Shop
WooCommerce Collections Block
Advanced Custom Fields
Learn how to power up your Search & Filter fields with ACF data.
Advanced Custom Fields Overview
Looking for version 2 documentation? Head to the
version 2 documentation site
.
Queries Overview
Queries
Queries are the backbone of your site. From search, to blogs, to products listings and more, they power your website in many different ways. With Search & Filter, you can select the different queries across your site, choose to modify them, and attach fields such as search and filters to them (optional). The most important…
Read more ->
: Queries Overview
September 4, 2022
Query Editor
Queries
Name When referencing the query throughout the site the name will be used. Tabs Location Define how a Search & Filter query integrates with your site. Query Modify the query options to control what your users will see. Taxonomies Apply taxonomy restrictions to your queries, or exclude specific taxonomies or terms from your results. Post…
Read more ->
: Query Editor
December 17, 2023
Live Search (Pro)
Queries
Settings Live Search Disable or enable the Live Search feature. When enabled, results will be updated without reloading the page. When disabled the page will reload. Update URL Updates the URL in the address bar to reflect the current search & filter state. Fully supports the browser history API, meaning you can press backwards and…
Read more ->
: Live Search (Pro)
October 15, 2024
Results Shortcode (Pro)
Queries
With the shortcode setting, you can display your results anywhere on your site by using a shortcode – and then customise the results using PHP templates in your theme folder. Enable Shortcodes Head to the Settings screen and enable the Shortcodes setting. By default they’re enabled already. Create a Query Set the location to Dynamic…
Read more ->
: Results Shortcode (Pro)
November 26, 2024
Archives
Queries
An archive is an automatically generated list of posts, available at various locations in your site. WordPress usually comes with some archives built in and ready to use, it’s also possible to create more. They are usually accessible via a specific URL, related to the archive type. There are two main types of archive that…
Read more ->
: Archives
September 6, 2022

---

## GenerateBlocks Extension - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/developer/changelogs/generateblocks-extension/

1.0.1
Fix – issue detecting the “load more” container when the looper container didn’t have a class.
Fix – PHP issue hooking into
loop_items
and not passing in a WP_Query instance.
Fix – issue with the “next page link” /
{next_posts_page_url}
dynamic tag not rendering when using Search & Filter queries
Fix – JS error in the block editor after deleting a connected Search & Filter query.
1.0.0
Init release
More From This Series
Developer
Queries
Fields
Theme Integration
Custom query integration
Changelogs

---

## Search & Filter Pro - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/developer/changelogs/search-filter-pro/

3.1.8
Hotfix – workaround for an issue introduced in the Beaver Builder extension.
3.1.7
Improvement – update integrations list.
Improvement – platform updates to support integrations.
3.1.6
Improvement – clearing a field is no longer affected by the auto submit delay.
Fix – an issue with rendering field previews in admin screens.
Fix – an issue with counts not updating correctly when using the indexer.
Fix – issues with incorrect position of our dropdown in some scenarios.
Fix – an issue where a license that was already removed via your account couldn’t not be disconnected in the plugin dashboard.
Fix – issues with the the autocomplete field not showing suggestions in certain conditions in admin previews.
3.1.5
New – support searching in radio, checkbox, select and button ACF fields when the indexer is enabled.
New – support using the “load more” field with WooCommerce Products Collections blocks, shortcodes & the shop page.
Fix – issues with live search and WooCommerce Products shortcodes.
Fix – issues when using search input types with ACF fields.
Fix – an issue when using the
post__in
filter with the indexer causing incorrect results to be displayed.
Fix – an issue where the indexer could stall.
Fix – issue where sort order stopped working when using post meta queries.
3.1.4
New – set field defaults and autodetect default values from archives or posts.
Improvement – better compatibility with block editor layouts and query loops.
Change – renamed the query and fields Javascript
remove()
function to
unload()
.
Fix – regression with ACF fields not generating their options properly.
Fix – issues when using WooCommerce Collections in the block editor.
Fix – script errors in the block editor.
Fix – update the indexer table to support longer values, matching the max length of taxonomy slugs.
3.1.3
Fix – issues with indexing some ACF fields.
Fix – error when the site can’t connect to Search & Filter update servers.
3.1.2
New – option to disable indexer sync when posts are updated on the frontend.
New – add a hook for overriding the shortcode template path.
Improvement – added warning about the maximum number of range options of 200 for select and radio ranges.
Improvement – stop using
getmypid()
when its not available (some hosting companies like Kinsta disable this function).
Fix – allow spaces as decimal or thousand seperators in range fields.
Fix – errors when using the same character for decimals and thousands.
Fix – issues with live search not working with the WooCommerce Shop when using non FSE themes.
Fix – issues with shortcodes pagination when used on the (static) homepage.
Fix – update the license check to use the new update server.
3.1.1
Fix – hotfix to remove the HPOS warning when using WooCommerce.
Fix – prevent litespeed cache from caching our indexer process leading to inaccurate indexer status.
Fix – issues with current selection values not showing in the selection field.
Fix – issues with plugin updates performed via the plugins screen.
Fix – update to using the new license server to work around hosting issues.
3.1.0
New – updates to support the integration with the Dynamic Content for Elementor plugin.
New – support for custom WooCommerce stock statuses in fields.
New – show out of stock option for WooCommerce fields.
New – filter on product tags, categories and brand archives.
Improvement – update the results shortcode template to automatically support the “load more” button
Improvement – add additional CSS properties to range sliders to prevent themes from overriding styling (Astra)
Improvement – click on range sliders to set automatically set the handle locations.
Improvement – add plugin action link to the settings page.
Improvement – stop disabling the checkbox on the plugins screen for the base plugin.
Fix – issues with indexing WooCommerce product variations.
Fix – an issue with the WooCommerce shop not completing ajax requests.
Fix – an issue with WooCommerce category fields when displaying hierarchically.
Fix – issues with WP 6.7 and loading translations too early.
Fix – auto submit was not working with the date picker.
Fix – issues when editing range fields, prompting for the field to be saved when no changes had been made.
Fix – issues with floating point calculations in range fields.
Fix – issues with date fields when connected to custom fields or ACF data – rebuild the indexer if you are using these.
Fix – an issue with autodetecting min/max with range fields.
Fix – links with URL fragments caused issues with live search.
3.0.6
Improvement – allow option for the indexer to build when loopback requests fail – enable via ->
settings
->
indexer
-> disable
use background process
Fix – an issue with some optimization plugins stripping out our initialisation JS.
Fix – the sort order field was not working when the indexer was enabled.
Fix – an issue when showing available meta keys.
Fix – prevent activating the Search & Filter base plugin if its a really old version (1.x).
Fix – some tables were not being uninstalled when the option to remove all data was enabled.
3.0.5
New – add option to hide fields when they don’t have any choices available.
New – improve text search for ACF fields and add support for searching inside ACF repeater fields.
New – add support for ACF taxonomy fields.
New – allow integration plugins to be downloaded directly from the integrations screen.
New – add ordering parameters to autocomplete fields (order suggestions alphabetically, ascending and descending)
Improvement – when checking for updates ensure all related plugin updates are also available.
Improvement – increase specificity of our range slider CSS classes for better consistency.
Change – JavaScript APIs have been restructured and renamed.
Fix – remove debugging tools warnings when using auto submit on fields.
Fix – load more button was not being affected by the width settings.
Fix – fields are now properly restored when they are inside a dynamic update section.
Fix – auto detect min/max for ranges was causing an error in admin screens.
Fix – indexer status was not correctly updated.
Fix – the search field would cause a double submit when the auto submit setting was enabled.
3.0.4
New – Fields – added “show count numbers” and “hide options with no results” to fields for post types, post statuses and post authors.
New – Fields – order field options by “count” when the indexer is enabled.
New – expose mount script to re-init our frontend JS when needed.
Fix – disable Query Monitor plugin output in our JSON api requests which were preventing ajax requests from being completed.
Fix – Fields – an issue where a field option would dissapear when using the indexer.
Fix – Fields – issues with hierarchical taxonomies showing the incorrect counts.
Fix – Queries – various errors thrown in the indexer when a field has certain conditions.
Fix – Queries – dynamic update settings weren’t showing when using archive display method
Fix – an issue with some of the dynamic update settings not appearing under certain conditions.
Fix – prevent adding to the browser history state if the search/filters didn’t change.
3.0.3
New – added Relevanssi integration.
Improvement – stability, speed and accuracy improvements for the indexer.
Fix – issues with the load more control not working properly in some circumstances.
Fix – issues with pagination not working in results shortcodes.
Fix – issue in our php results template file causing issues in some setups.
Fix – an issue with the pagination parameters appearing multiple times in a URL.
Fix – issues with Cron schedules.
3.0.2
Improvement – add message when a license has no activations left.
Improvement – show the results shortcode and allow for copy and paste in the query editor.
Fix – issue with the toggle icon not appearing in labels.
Fix – fatal error when using
post__in
in queries connected to S&F.
3.0.1
New – allow disabling the “scroll to” option in the query settings.
New – add support for ACF date picker and date time picker fields.
New – add sorting options for custom fields + ACF fields.
Improvement – prevent disabling the base plugin unless the pro plugin is disabled.
Fix – various issues with the indexer and showing the indexer status.
Fix – an issue where custom fields were showing a limited number of options.
3.0.0
Fix – issue with the loading icon position.
Fix – issue with count formatting.
3.0.0-beta-4
Update – platform updates to support page builder integrations.
3.0.0-beta-3
Fix – an issue with the cache table not being created correctly.
3.0.0-beta-2
New – indexer & dynamic fields.
New – WooCommerce fields and integration options.
New – support for ACF repeater fields, flexible content, group and relationship fields.
New – add support for authors in fields.
Fix – issue with custom fields not working correctly.
Fix – issues with ACF fields not working correctly.
Fix – issue with custom field urls not working for taxonomy fields.
More From This Series
Developer
Queries
Fields
Theme Integration
Custom query integration
Changelogs

---

## Documentation - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/?query-0-page=6

Looking for an
integration
? Checkout the
integrations documentation
below.
Getting Started
Get to grips with basics and build your first search form.
Queries
Find out what Queries are and how you can leverage them to build listings.
Fields
Learn about the different fields types and how to set them up.
Styles Presets
Learn how to create your own styles presets.
FAQ
Some of our most commonly asked questions.
Block Editor
Learn how to create your fields & queries directly in the Block Editor.
Developer
Documentation for advanced integrations & APIs.
Known Issues
Known issues with third party software and how to work around them.
Integrations
Integrations
Find out the best way to get up and running using your favorite tools.
WooCommerce
Get up an running with WooCommerce, however you use it.
Advanced Custom Fields
Learn how to power up your Search & Filter fields with ACF data.
Looking for version 2 documentation? Head to the
version 2 documentation site
.
Integrations
Integrations are regularly updated – checkout the guides below. Elementor Advanced Custom Fields (ACF) WPML Relevanssi Beaver Builder Dynamic Content for Elementor Polylang (coming soon) Divi (coming oon) WPBakery Page Builder (coming soon) Easy Digital Downloads (coming soon)
Read more ->
: Integrations
September 30, 2024
Guides
A collection of step by step guides to get you started with using Search & Filter – we’re working on these: Fields Queries Integrations Migration
Read more ->
: Guides
September 4, 2022
Theme Integration
Developer
Search & Filter supports integration with themes by allowing them define a set of styles to use. This allows theme builders to provide a seamless integration of their theme styling with Search & Filter. How it works If a theme opts in to supporting Search & Filter styles then a “Theme” styles preset will be…
Read more ->
: Theme Integration
July 5, 2023
Custom query integration
Developer
Creating a custom query integration requries several steps depending on your needs. Setting up your query To connect Search & Filter with your query you will need to add an argument to the query itself with the name search_filter_query_id. The value of this argument should be the ID of of the Search & Filter query…
Read more ->
: Custom query integration
September 29, 2023
Changelogs
Developer
Below are the changelogs for the Search & Filter plugins and their extensions.
Read more ->
: Changelogs
January 11, 2025
Troubleshooting
FAQs
Checking for conflicts One of the first steps when troubleshooting is checking for conflicts with plugins and themes. The WordPress ecosystem is vast, and there is no reliable way to ensure that a specific plugin will work well with another, or a specific theme. By using the WordPress APIs and coding standards, we can improve…
Read more ->
: Troubleshooting
November 28, 2024

---

## Create a Query - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/getting-started/create-a-query/

Search & Filter
relies heavily on the creation of
Queries.
Using our
Query Builder
you can easily create queries and fine tune them to display content on your site.
Combine Search & Filter
Queries
with Search & Filter
Fields
to allow your visitors filter down
exactly
what they’re looking for, keeping them on your site for longer and increasing conversions!
Note:
For this guide, you’ll need to ensure that
Search & Filter
version 3 is installed and up to date.
Navigate to the Query Builder
Log into your WordPress admin dashboard.
Hover over the
Search & Filter
menu on the left-side of the screen and click on the
Queries
option.
Click on the
Add new
button at the top of the page.
Configure the Query Settings
Next, you’ll need to add a name for your query. This name won’t be visible on the front end of your site, however, it will be used by the
Search & Filter
plugin to differentiate this query from other queries.
Check that the
Enabled
switch is on. This switch is on by default when you first create a query, but keep in mind that if this switch is off, the
Query
won’t be available to use.
In the
Location
tab, you can determine and change the expected
Location
of the query as well as the expected source of the WordPress query.
In short, our plugin can identify and modify a WordPress query to showcase different results on a page based on a user’s interaction.
For this example, we’ll leave everything as it is and use the default options (including keeping the
Autodetect query loop
option turned on).
If you’d like to find out more information about what these settings do, and how you can utilize them, you can click here.
Also, you can find more on how to create a query that relies on a
Shortcode
here.
Next, click on the
Query
tab.
There are a lot of different options here, so let’s try to break them down:
Use Indexer
(Pro)
:
this setting will enable Search & Filter’s
Indexer.
You can find out more about the
Indexer
here, but in short, this feature facilitates faster and dynamic search and filtering. For this example, we’ll keep the feature off and rely on WordPress’ query.
Post types:
in this field, you’ll need to specify the expected post types of the query. You can choose to add multiple post types, like
Media
and
Pages,
as well as custom post types.
Note:
Some
Location
types are locked into the post type of the archive itself (e.g. WooCommerce Shop only allows for Products).
Depending on the post types added to this field, you’ll get different results when searching and/or filtering a query.
For this guide, we’ll use the default
Posts
option.
Post status:
similar to
Post types
, this field allows you to choose multiple possible post statuses to search from.
We’ll keep the default option of
Published
for the time being.
Posts per page:
this field allows you to change the number of returned posts per page for each query. The maximum number is 100. We’ll be using the default 10 for now.
Sort order:
this option allows you to fine-tune the query further so that the appearance order of posts after a search or filter interaction has occurred is specified. There’s a long list of options you can choose to order based on, but for now, we’ll keep this option turned off. Here’s a screenshot of the options, though, for reference:
Sticky posts:
you can choose to
Ignore
sticky posts from the query. There are some extra options for this field like
Excluding
them,
Showing
them, or
Only
take into consideration sticky posts.
For now, we’ll use the default option, which is
Ignore.
Field relationship:
this setting allows you to adjust the behavior of included fields for a query. In short, for posts that utilize added fields (e.g. WooCommerce products that have product category and product tag), this setting will determine the relationship the fields have between them.
We’ll use the default option for now, but if your posts utilize multiple post fields, you can read our document here for more information on how you can use this.
Exclude Current Post:
this switch is set to
Yes
by default, and will exclude the post that the
Query
is added to.
When you’re done with the
Query
tab, you can then click on the
Save
button to save the query. Regarding the tabs that we didn’t utilize in this example:
The
Taxonomies
and
Post Meta
fields allow you to further fine-tune the query so that specific taxonomies and post meta are taken into account when the
Query
is utilized. You can learn more about how to configure these fields here.
If not used, the
Query
will rely on WordPress query’s default options for these fields.
The
Live Search
tab is a feature that was upgraded in version 3 of Search & Filter. It allows your users to complete searches without triggering a page refresh. This feature is great if you’re looking to create a dynamic search for your site, but we won’t use it for this example.
Click here to find out more about this feature.
Well done! You’ve just created your first query! This is how it will look like after you have clicked on the
Save
button:
The highlighted number is the
Query’s
ID. This ID is required for some custom configuration and code snippets, but for the time being, you can ignore it.
Connected Fields
If you scroll down below the query builder, you’ll notice the
Connected Fields
section:
This is one of the places where you can create
Fields
to search and filter the
Query
you created.
Continue to the next guide about creating fields.
On This Page
Navigate to the Query Builder
Configure the Query Settings
Connected Fields
More From This Series
Getting Started
Overview
Installation
Create a Query
Create a Field
Building a Layout

---

## Fields Overview - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/fields/fields/

Fields allow your visitors to interact with queries on your site, enabling them to drill down to find the information they are looking for.
This means they spend less time looking for the information they need.
Field types
There are 5 different types of fields:
Search
,
Choice
,
Range
(pro),
Advanced
and
Control
.
Search fields
allow for text input – users can type what they are looking for and the results will be refined based on the search terms.
Choice fields
allow users to select from multiple options to find what they are looking for.
Range fields
allow users to select between a numerical range
Advanced fields
usually don’t fall into the categories above, and include things like date pickers and map search.
Control fields
usually interact with the query in different ways, such as submitting a search, resetting the fields, or changing the page of results.
Learn more about the different field types.
Adding fields to your site
Reusable fields
Reusable fields can be created via our admin pages and re-used throughout your site.
They’re great for all kinds of sites as they work with any theme/plugin combination, and can be added to your site via shortcodes or blocks.
You can create reusable fields via our admin field editor.
Checkout the guide on creating reusable fields.
Block editor fields
Block editor fields allow you to create your fields directly in the block editor and they have the same options as our reusable fields.
The only difference with these are that blocks only live on the post/page where they are created.
There are 5 blocks to match our field types:
Search
Choice
Range
(pro)
Advanced
Control
On This Page
Field types
Adding fields to your site
Reusable fields
Block editor fields
Page builders (Pro)
More From This Series
Fields
Fields Overview
Field Editor
Field Types

---

## Block Editor Overview - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/block-editor/block-editor-overview/

Search & Filter comes with deep support and integration with all of core WordPress including the Block Editor, as standard.
Field Blocks
There are 6 field blocks available in the Block Editor:
Search Field Block
– including text input and autocomplete controls.
Choice Field Block
– including select, checkbox, radio and button controls.
Range Field Block
(Pro) – including range slider, radios and selects.
Advanced Field Block
– includes the date picker.
Control Field Block
– includes submit, reset, sort, load more and current selection inputs.
Reusable Field Block
– allows for re-using existing fields throughout your site.
These blocks allow you to build your fields and queries directly in the Block Editor, ensuring you never break your workflow.
Learn How to Add Fields
Read More about Field Types
Queries & The Query Loop
Search & Filter Supports the Query Loop out of the box, allowing you to create highly customised queries using our own query builder, and then connecting them to fields to create rich search and filtering experiences using the
Query Loop Block
.
Query Loop Variations
Query loop variations are also supported via the Query Selector inspector control.
Learn How to Create Queries in the Block Editor
Read More about Queries
Full Site Editing
Full Site Editing (FSE) allows you to use the block editor to design templates for the archives on your site.
Search & Filter supports FSE and allow you to create rich search and filter experiences for your archives.
Block Editor Plugins
Search & Filter also supports a number of Block Editor plugins and their own Query Loop implementations:
WooCommerce Collections Block
GenerateBlocks
Greenshift
On This Page
Field Blocks
Queries & The Query Loop
Query Loop Variations
Full Site Editing
Block Editor Plugins
More From This Series
Block Editor
Block Editor Overview
Block Editor – Add Fields
Block Editor – Create Queries

---

## Theme Integration - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/developer/theme-integration/

Search & Filter supports integration with themes by allowing them define a set of styles to use.
This allows theme builders to provide a seamless integration of their theme styling with Search & Filter.
How it works
If a theme opts in to supporting Search & Filter styles then a “Theme”
styles preset
will be created – this preset cannot be edited or deleted and always appears at the top of the styles presets lists.
Providing a theme style gives users visually pleasing and sensible defaults when working with your theme and Search & Filter. Users are still able to create their own styles presets if they wish.
There are two ways to add default styling support for Search & Filter:
Via
theme.json
The default framework structure of theme JSON looks something like this:
{
"
$schema
"
:
"
https://schemas.wp.org/trunk/theme.json
"
,
"
version
"
:
2
,
"
settings
"
:
{},
"
styles
"
:
{
"
blocks
"
:
{},
"
color
"
:
{},
"
elements
"
:
{},
"
spacing
"
:
{},
"
typography
"
:
{}
}
}
Note:
values and theme settings have been removed for simplicity.
To add support for Search & Filter styles presets requires adding a sub property
plugins
to the
styles
property, followed by another property with our plugin slug
search-filter
.
Adding this to the styles section would look like this:
{
"
$schema
"
:
"
https://schemas.wp.org/trunk/theme.json
"
,
"
version
"
:
2
,
"
settings
"
:
{},
"
styles
"
:
{
"
blocks
"
:
{},
"
color
"
:
{},
"
elements
"
:
{},
"
spacing
"
:
{},
"
typography
"
:
{},
"
plugins
"
:
{
"
search-filter
"
:
{
"
color
"
:
{
"
text
"
:
"
#3C434A
"
,
"
background
"
:
"
#fff
"
,
"
active-text
"
:
"
#fff
"
,
"
active-background
"
:
"
#167DE4
"
,
"
label-text
"
:
"
#3C434A
"
,
"
secondary
"
:
"
#3C434A
"
,
"
primary-accent
"
:
"
#BBBBBB
"
,
"
secondary-accent
"
:
"
#888888
"
,
"
tertiary-accent
"
:
"
#333333
"
}
}
}
}
}
Via
add_theme_supports
We can also use the PHP function
add_theme_supports
to set the Theme preset style:
$
search_filter_styles
=
array
(
'
color
'
=>
array
(
'
text
'
=>
'
#3C434A
'
,
'
background
'
=>
'
#ffffff
'
,
'
active-text
'
=>
'
#ffffff
'
,
'
active-background
'
=>
'
#167DE4
'
,
'
label-text
'
=>
'
#3C434A
'
,
'
secondary
'
=>
'
#3C434A
'
,
'
primary-accent
'
=>
'
#BBBBBB
'
,
'
secondary-accent
'
=>
'
#888888
'
,
'
tertiary-accent
'
=>
'
#333333
'
)
)
;
add_theme_support
(
'
search-filter-styles
'
,
$
search_filter_styles
)
;
Supported styles
Currently Search & Filter supports customising the color scheme as shown in the examples above
Colors
There are currently 6 colors that can be defined which are used across all our UI widgets. It might be a good idea to design the preset via our styles editor and then copy the color references into your theme settings.
Name
Property
Text
text
Background
background
Active text
active-text
Active background
active-background
Label text
label-text
Secondary
secondary
Primary accent
primary-accent
Secondary accent
secondary-accent
Tertiary accent
tertiary-accent
Borders
These sections will be added once version 3 is out of beta.
This will include border style and thickness (colors are already supported above).
Spacing
These sections will be added once version 3 is out of beta.
This will include paddings and margin.
Icons
These sections will be added once version 3 is out of beta.
It will be possible to replace any of the icons used in our plugin with icons defined by the theme.
On This Page
How it works
Via theme.json
Via add_theme_supports
Supported styles
Colors
Borders
Spacing
Icons
More From This Series
Developer
Queries
Fields
Theme Integration
Custom query integration
Changelogs

---

## Field Editor - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/fields/field-editor/

The field editor allows you to create, edit and design the frontend fields on your site.
Access the field editor via the Search & Filter
Dashboard
, then choose
Fields
in the main menu.
If you are using the
block editor
, you can access all the same settings and features directly via our block equivalents.
Name
When referencing the field throughout the site the name will be used.
It will not be visible on the frontend
It can be used in shortcodes (be careful when changing it though!)
Will be used when referencing the field in blocks and other frontend widgets and modules (for example, in an Elementor widget)
Type
This is where you can change the main field type.
Search
– allows for free text input to search for posts matching the search term.
Choice
– allows for a single selection or multiple selection from a set of options.
Range
– allow users to select a single numerical value within a specified range, or select two values to define a range to filter.
Advanced
– have more unique or complex functionality than the other field types.
Control
– interact with the query in different ways, such as submitting a search, resetting the fields, or changing the page of results
Learn more about field types.
Settings
This is where you will see a fully interactive preview of your field.
It will be populated by the data types you have chosen and will display any styling options you have applied.
Read more about field types
Styles
Clicking the styles tab will reveal a panel containing only styles settings. You can adjust design settings for the heading, description and input fields directly.
Design options include:
Multiple color options, for borders, background colors, hover colors and more.
Scale up and down your field sizes preserving padding and borders.
Paddings and margins
+ more coming soon!
Preview
This is where you will see a fully interactive preview of your field.
It will be populated by the data types you have chosen and will display any styling options you have applied.
Actions
You can save, update, or delete actions from the actions toolbar.
On This Page
Name
Type
Settings
Styles
Preview
Actions
More From This Series
Fields
Fields Overview
Field Editor
Field Types

---

## Styles Editor - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/styles/styles-editor/

More From This Series
Styles
Styles Overview
Styles Editor

---

## Elementor Search & Filtering - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/integrations/elementor/

The
Search & Filter – Elementor Extension
allows for seamless integration between Elementor and Search & Filter.
With this extension, Search & Filter will now be able to directly integrate and filter the following Elementor widgets:
Loop Grid
Loop Carousel
Posts
Archive Posts
Products
Archive Products
Portfolio
Install + activate the extension
To get started first we need to enable the integration in our integrations screen.
Ensure you have
Elementor
enabled.
Then from the Integrations screen, click
install extension
.
The extension plugin will be automatically downloaded in the background and then enabled.
If there are any issues downloading the extension, you can
download it from your account
and install it manually.
Create a query
Head to
Queries
in the main navigation, then press
Add New
to create a new query.
Ensure that location is set to
dynamic
and then choose
Elementor Widget
from the query dropdown:
Give your query a
name
, hit
save
and your query is good to go.
There are a lot of settings
to fine tune your results.
Create a field
After saving your query, you’ll find your connected fields below. There won’t be any initially – press
Add New
to create one.
From here you can create as many fields as you need and connect them to the same query.
When creating fields for queries, ensure the
query integration
option is set to the correct query.
Read more about fields here
.
Adding fields to your site
Once you’ve created some fields, you can add them to your Elementor site using the
Search & Filter Field
widget.
Note:
using shortcodes to place fields can lead to unexpected behaviour, it’s always best to use the Field widget.
Once you’ve added the widget to your page you can choose the field you created earlier from the dropdown:
Filter the Loop Grid + Carousel
It is required to have
Elementor Pro
installed to use the The Loop Grid and Carousel.
To integrate with the loop grid + carousel, ensure that you’ve set the
Elementor Module
option in your query
as described
above
.
The next step is to connect your loop grid or carousel to your Search & Filter query:
Head to the
Query
panel
Choose
Search & Filter
as the source
Then choose your query from the dropdown
Once connected Search & Filter is now ready to work with your grid + carousel.
Filtering Archives
Search & Filter will automatically integrate with archives built with Elementor.
Usually for an Archive template you’ll want to use an archive widget:
Archive Posts
Archive Products
Or you can use one of the following widgets:
Loop Grid
Loop Carousel
Posts
Products
For these widgets, it’s recommended to set to set the
Query Source
to use the
Current Query
:
When setting up an archive using the
Current Query
or using the Archive Posts or Archive Products widgets, the Search & Filter query must also be configured to use the archive query:
On This Page
Install + activate the extension
Create a query
Create a field
Adding fields to your site
Filter the Loop Grid + Carousel
Filtering Archives
More From This Series
Integrations
Elementor
Beaver Builder
Relevanssi
GenerateBlocks
WPML
Polylang
Dynamic Content for Elementor
Easy Digital Downloads
Divi
WPBakery Page Builder

---

## Documentation – Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/faqs/

Looking for an
integration
? Checkout the
integrations documentation
below.
Getting Started
Get to grips with basics and build your first search form.
Overview
Installation
Create a Query
Create a Field
Building a Layout
Queries
Find out what Queries are and how you can leverage them to build listings.
Queries Overview
Query Editor
Live Search (Pro)
Results Shortcode (Pro)
Archives
Fields
Learn about the different fields types and how to set them up.
Fields Overview
Field Editor
Field Types
Styles Presets
Learn how to create your own styles presets.
Styles Overview
Styles Editor
FAQ
Some of our most commonly asked questions.
What’s new in version 3?
Can I use my license on local or staging sites?
Debugging
Upgrading to Pro version 3 (from v2)
Troubleshooting
Block Editor
Learn how to create your fields & queries directly in the Block Editor.
Block Editor Overview
Block Editor – Add Fields
Block Editor – Create Queries
Developer
Documentation for advanced integrations & APIs.
Queries
Fields
Theme Integration
Custom query integration
Changelogs
Known Issues
Known issues with third party software and how to work around them.
WP Engine
WP Rocket
Integrations
Integrations
Find out the best way to get up and running using your favorite tools.
Elementor
Beaver Builder
Relevanssi
GenerateBlocks
WPML
Polylang
Dynamic Content for Elementor
Divi
WPBakery Page Builder
Easy Digital Downloads
WooCommerce
Get up an running with WooCommerce, however you use it.
WooCommerce Overview
WooCommerce Shop
WooCommerce Collections Block
Advanced Custom Fields
Learn how to power up your Search & Filter fields with ACF data.
Advanced Custom Fields Overview
Looking for version 2 documentation? Head to the
version 2 documentation site
.
What’s new in version 3?
FAQs
Read more ->
: What’s new in version 3?
September 20, 2024
Can I use my license on local or staging sites?
FAQs
Local sites and some supported staging sites will not count towards your activation limit. That means you can activate Search & Filter and receive updates on those sites regardless of your activation limit. Local sites We support local URLs that follow the following patterns: Staging sites We support stagings sites for the following hosts: We…
Read more ->
: Can I use my license on local or staging sites?
October 10, 2024
Debugging
FAQs
To access your data for debugging follow these steps: Enable debugging tools Head to the Search & Filter settings screen, and enable the debugging tools. Export Data Head to the page with your query and filters and click the Search & Filter admin bar menu item to open the sidebar. At the bottom of the…
Read more ->
: Debugging
September 29, 2024
Upgrading to Pro version 3 (from v2)
FAQs
This is a guide on how to upgrade from version 2 to version 3. Notice – we have extended our end of life dates while we prepare the migration tool. Version 2 will continue to be supported until at least December 2025, there is no immediate requirement to upgrade to version 3. Upgrading from version…
Read more ->
: Upgrading to Pro version 3 (from v2)
July 17, 2024
Troubleshooting
FAQs
Checking for conflicts One of the first steps when troubleshooting is checking for conflicts with plugins and themes. The WordPress ecosystem is vast, and there is no reliable way to ensure that a specific plugin will work well with another, or a specific theme. By using the WordPress APIs and coding standards, we can improve…
Read more ->
: Troubleshooting
November 28, 2024

---

## Documentation – Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/known-issues/

Looking for an
integration
? Checkout the
integrations documentation
below.
Getting Started
Get to grips with basics and build your first search form.
Overview
Installation
Create a Query
Create a Field
Building a Layout
Queries
Find out what Queries are and how you can leverage them to build listings.
Queries Overview
Query Editor
Live Search (Pro)
Results Shortcode (Pro)
Archives
Fields
Learn about the different fields types and how to set them up.
Fields Overview
Field Editor
Field Types
Styles Presets
Learn how to create your own styles presets.
Styles Overview
Styles Editor
FAQ
Some of our most commonly asked questions.
What’s new in version 3?
Can I use my license on local or staging sites?
Debugging
Upgrading to Pro version 3 (from v2)
Troubleshooting
Block Editor
Learn how to create your fields & queries directly in the Block Editor.
Block Editor Overview
Block Editor – Add Fields
Block Editor – Create Queries
Developer
Documentation for advanced integrations & APIs.
Queries
Fields
Theme Integration
Custom query integration
Changelogs
Known Issues
Known issues with third party software and how to work around them.
WP Engine
WP Rocket
Integrations
Integrations
Find out the best way to get up and running using your favorite tools.
Elementor
Beaver Builder
Relevanssi
WPML
GenerateBlocks
Polylang
Dynamic Content for Elementor
Easy Digital Downloads
Divi
WPBakery Page Builder
WooCommerce
Get up an running with WooCommerce, however you use it.
WooCommerce Overview
WooCommerce Shop
WooCommerce Collections Block
Advanced Custom Fields
Learn how to power up your Search & Filter fields with ACF data.
Advanced Custom Fields Overview
Looking for version 2 documentation? Head to the
version 2 documentation site
.
WP Engine
Known Issues
WP Engine has a feature which prevents long queries from being executed. This is called the Long Query Governor. Unfortunately this feature often prevents our queries from executing correctly, either when building the indexer via wp-admin or when running our queries on the frontend of your site. You might see an error in your logs…
Read more ->
: WP Engine
October 17, 2024
WP Rocket
Known Issues
WP Rocket has a feature to delay JavaScript execution: Using this feature with Search & Filter can result in our search & filter fields not displaying at all. To work around this, we can add some rules to exclude our JavaScript files and objects. In the Excluded JavaScript Files section: Add the following rules (copy…
Read more ->
: WP Rocket
December 31, 2024

---

## Create a Field - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/getting-started/create-a-field/

After you have created your first query (link to the article), it’s time to get started with creating a field. While Search & Filter
Queries
are the backbone of the filtering and search functionality of our plugin,
Fields
allow your users to interact with the set options. There are various types of fields, but for this example, we’ll create a 3 fields: a
search
,
choice
(filter), and
control
(submit) field.
The process is very similar for all fields, so we’ll discuss one in detail and then breeze through the rest.
Note:
Similar to the Search & Filter
Queries,
fields have multiple formats that can be used to add them to your site. Check out our in-depth article on fields to learn more.
For this example, we’ll review the
Shortcode
and
Block
options. Those are incorporated with WordPress by default and can be utilized without any added integrations.
Create a Search Field
To create a search field:
Log into your WordPress admin dashboard.
Go to the
Search & Filter > Fields
page.
Click on the
Add New
button at the top of the page.
The Field Editor will appear. First, you’ll need to make sure to add a name for your field and choose its type. For this example, we’ll use the
Search
type.
Check that the
Enabled
switch is on. It will be on by default, however, please note that if this option is turned off, the field will not be available to use on your site:
You’ll notice that there’s a live preview of the field in the middle of the page, and the settings can be found on the right-side menu. Let’s go through the different settings together:
Query (Required):
this setting creates a connection between this field and the query that you’ll be using to filter your posts. This is one of the most important settings, so make sure to click on the dropdown menu and choose the relevant query.
If no changes are made, our plugin will automatically detect the most recent query you have created.
Data Type:
this field controls what data type the search should focus on. There are multiple options available, but for the time being, we’ll use the default
Post Attributes
option. This data type utilizes common posts’ attributes like their title, content, type, and even status.
Not all options can be used in unison, though. We’ll need to specify which one is preferred in the following field.
Data Source:
this field sets what should be the source of the search. For example, when the data type is set to
Post Attributes,
the data source has different options available. For this example, we’ll use the default option – which is the
Post Title + Content
one.
This means that when a user types a keyword to search, the query will search through your posts’
Post Title + Content
to output relevant results.
URL Name (Pro):
this field allows you to edit the URL name for the field. By default, Search & Filter uses the following format by default:
yourdomain.com/page/?_s=”search-term
”
This setting will change the /?_s term to the one you specify in this field.
Note:
this setting only accepts characters a-z, underscores, and/or hyphens.
Input Type:
here, you can change what is the expected input type for this field. By default, there are two options available,
Text
and
Autocomplete (Pro).
For this example, we’ll use the
Text
option, but you can read more about how to configure the
Autocomplete
setting here.
Placeholder Text:
you can specify what the placeholder text of the field should be here. We’ve added a sample phrase here, but you can keep this empty if you don’t want to use placeholder text.
Show icon:
you can turn this off if you’d like to hide the magnifying glass icon inside the search field. We’ll keep this on for this example.
Label:
similar to the
Placeholder Text
field, you can change the text of the label. By default, the text is set to
New field.
We’ll change it to a different text for this example.
There are some extra options relevant to this field:
Show label
: this is on by default but you can turn it off if you don’t want to use a label for your field. We’ll keep this on for this example.
Toggle input visibility:
this switch controls whether the search field can be hidden so that only the
Label
is visible unless a user interacts with it. We’ll keep this off for this example.
Note:
This option is only available when the
Show label
switch is on.
Show description:
this switch allows you to enter a sub-label for the search field. It’s off by default, but if you turn it on, you can specific a description for the field and it will look like this:
We’ll keep it off for this example.
Width:
here, you can set what percentage of its container’s width you’d like this field to fill.
Depending on how you’re designing your site’s pages, it’s common for WordPress themes to allow the use of empty elements that can help with the design of a page’s layout. Even if an element isn’t used, the element will try to fill in the space of its container based on this setting.
For now, we’ll keep it to 100% – which is also the default option – but you can find out more about changing the style of a field here.
Auto submit:
keeping this switch on by default will automatically submit the value of the field every time a user has finished typing. It’s great if you’re looking to create a dynamic search experience, however, keep in mind that the auto submit delay is fairly small and it can cause unwanted keywords to be submitted.
We’ll turn it off for this example as we’re aren’t creating a
Live Search
form.
Auto Submit Delay:
this field allows you to adjust the auto submit delay. You’ll need to add the field in milliseconds (i.e. 1 second = 1000 milliseconds).
Default Value:
this setting allows you to preselect an option in a particular field. This allows you to showcase the query results already filtered with a specific option. You can configure it to:
–
Inherit from current location:
this option will allow you to activate switches to automatically inherit the value from the current archive, and/or the current post, page, or custom post type. You can also allow the filter to be initially applied to the query so that the results of the query are filtered based on those options.
–
Custom:
you can use this option to add a custom, default value instead.
For this example we will not add a default value and keep the option set to
None.
Add a class:
Lastly, you can add a custom CSS class to this field. This is great if you’re looking to make any custom CSS changes or if you’d like to target that element with a custom script.
We’ll keep this empty by default.
When you’re done making all the needed changes, click on the
Save
button and you’ve just completed your first search field. Well done!
Control Field
The
Control Field
is essentially a button that allows your users to complete certain actions to control the rest of the search and/or filter fields. For example, you can create a submit button for users to be able to use to submit their search terms, a reset button to reset all the previous filters, and even a field that your users can use to sort the output of a query.
For this example, we’ll create a submit button. Keep in mind that the first few steps are identical to creating a
Search Field
. You can review them again below for quick reference:
Log into your WordPress admin dashboard.
Go to the
Search & Filter > Fields
page.
Click on the
Add New
button at the top of the page.
The Field Editor will appear. First, you’ll need to make sure to add a name for your field and choose its type. For this example, we’ll use the
Search
type.
Check that the
Enabled
switch is on. It will be on by default, however, please note that if this option is turned off, the field will not be available to use on your site:
You’ll notice that there’s a live preview of the field in the middle of the page, and the settings can be found on the right-side menu. Let’s go through the different settings together:
Query (Required):
this setting creates a connection between this field and the query that you’ll be using to filter your posts. This is one of the most important settings, so make sure to click on the dropdown menu and choose the relevant query.
If no changes are made, our plugin will automatically detect the most recent query you have created.
Control Type:
this dropdown allows you to set the type of the control field. Currently, we support the types highlighted in the screenshot:
For this example, we’ll choose the
Submit
option, but you can read more about the available control types and how to use them here.
Label:
You can change the text of the button here. We’ll use the text
Submit
for this article.
Description:
You can switch on the option to showcase a description for the field. We’ll keep this option off for this example.
Dimensions:
You can set the percentage of the width the field fills. For this example, we’ll use the 100% option.
Add a class:
In this field, you can add a custom CSS class in your control field.
When you’ve completed all the needed changes, you can click on the
Save
button to proceed.
Now, we’re ready to add the query and fields we’ve created to a page and complete our search form.
Some notes:
For styling changes, you’ll need to click on the black and white circle icon at the top of the menu:
You can find out more about changing the style of a field here.
After creating a field, there are two ways to add them to the page:
Use a
Reusable field
block and choose the field you just created. The block will automatically pick up all the options you set in this guide and ensure it’s properly connected to the needed query.
Use a
Shortcode.
You can find the shortcode code by navigating to the
Search & Filter > Fields
and then either clicking on the field you just created and scrolling down to find the
Info
section or clicking on the three dots on the right side of the field and then on
Copy shortcode
option as highlighted below:
We’ll go into detail on how to add those to a page in the next guide.
On This Page
Create a Search Field
Control Field
More From This Series
Getting Started
Overview
Installation
Create a Query
Create a Field
Building a Layout

---

## WPML Extension - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/developer/changelogs/wpml-extension/

1.0.0
Initial release to support Search & Filter Version 3
More From This Series
Developer
Queries
Fields
Theme Integration
Custom query integration
Changelogs

---

## Installation - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/getting-started/installation/

Uploading via the WordPress Dashboard
Navigate to the ‘Add New’ in the plugins dashboard
Navigate to the ‘Upload’ area
Select
search-filter.zip
or
search-filter-pro.zip
from your computer
Click ‘Install Now’
Activate the plugin in the Plugin dashboard
Using FTP
Download
search-filter.zip
/
search-filter-pro.zip
Extract the
search-filter
/
search-filter-pro
directory to your computer
Upload the
search-filter
/
search-filter-pro
directory to the
/wp-content/plugins/
directory
Activate the plugin in the Plugin dashboard
On This Page
Via the plugins page
Uploading via the WordPress Dashboard
Using FTP
More From This Series
Getting Started
Overview
Installation
Create a Query
Create a Field
Building a Layout

---

## Archives - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/queries/archives/

An archive is an automatically generated list of posts, available at various locations in your site. WordPress usually comes with some archives built in and ready to use, it’s also possible to create more.
They are usually accessible via a specific URL, related to the archive type.
There are two main types of archive that our plugin supports:
Post Type archives
Taxonomy archives
Post Type Archives
WordPress comes with a few post types built in, some examples are:
Posts
Pages
Media
Custom Post Types
However not all of them have archives. By default, only
Posts
has an archive ready to use, more commonly reffered to as the
blog
. Visitors can access a list of all your posts that will stay up to date as your create more posts.
Blog
The blog is the post type archive for regular posts and can be located in different places on your site depending on your site settings.
In a default WordPress installation, this will be your homepage, eg:
yoursite.com
However, the location can be changed by changing a WordPress setting via the dashboard.
Custom Post Types
Custom post types are useful for adding different kinds of data to your site. Much like the Posts post type, you can enable archives for your custom post types so that they appear on the frontend of your site.
An example might be a Book post type, which could be accessible at a URL:
yoursite.com/books/
Many plugins utilise custom post types. To enable archives for a custom post type, ensure that the
public
property is set to
true
.
Taxonomy Archives
The most commonly known taxonomies are Tags and Categories, but they inlcude more than just those – plugins and themes will often create taxonomies that behave like tags and categories, and it also possible to create your own.
Tags & Categories
Like the Blog archive, Tag and Category archives come built in to your WordPress site. Once you have some posts that are assigned to tags and categories, you can find them at their repective URLs:
yoursite.com/tags/…
yoursite.com/categories/…
Custom Taxonomies
Custom taxonomies can be created in your site to as a way assigning additional information to you posts, pages and custom post types.
By enabling the
has archive
option in your custom taxonomy, you’ll be able to display their archives on the frontend just like tags and categories.
You might be able to access a Genre taxonomy via a URL such as:
yoursite.com/genre/…
On This Page
Post Type Archives
Blog
Custom Post Types
Taxonomy Archives
Tags & Categories
Custom Taxonomies
More From This Series
Queries
Queries Overview
Query Editor
Live Search (Pro)
Results Shortcode (Pro)
Archives

---

## Documentation - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/#h-integrations

Looking for an
integration
? Checkout the
integrations documentation
below.
Getting Started
Get to grips with basics and build your first search form.
Overview
Installation
Create a Query
Create a Field
Building a Layout
Queries
Find out what Queries are and how you can leverage them to build listings.
Queries Overview
Query Editor
Live Search (Pro)
Results Shortcode (Pro)
Archives
Fields
Learn about the different fields types and how to set them up.
Fields Overview
Field Editor
Field Types
Styles Presets
Learn how to create your own styles presets.
Styles Overview
Styles Editor
FAQ
Some of our most commonly asked questions.
What’s new in version 3?
Can I use my license on local or staging sites?
Debugging
Upgrading to Pro version 3 (from v2)
Troubleshooting
Block Editor
Learn how to create your fields & queries directly in the Block Editor.
Block Editor Overview
Block Editor – Add Fields
Block Editor – Create Queries
Developer
Documentation for advanced integrations & APIs.
Queries
Fields
Theme Integration
Custom query integration
Changelogs
Known Issues
Known issues with third party software and how to work around them.
WP Engine
WP Rocket
Integrations
Integrations
Find out the best way to get up and running using your favorite tools.
Elementor
Beaver Builder
Relevanssi
GenerateBlocks
WPML
Polylang
Dynamic Content for Elementor
Divi
WPBakery Page Builder
Easy Digital Downloads
WooCommerce
Get up an running with WooCommerce, however you use it.
WooCommerce Overview
WooCommerce Shop
WooCommerce Collections Block
Advanced Custom Fields
Learn how to power up your Search & Filter fields with ACF data.
Advanced Custom Fields Overview
Looking for version 2 documentation? Head to the
version 2 documentation site
.
Overview
Getting Started
Installation If you are familiar with WordPress, login to your site and search/install the Search & Filter plugin from the plugins page (once we’re out of beta). For more details, you can read our step by step installation instructions. The basics There are two main concepts that drive this plugin: Queries Queries are the backbone…
Read more ->
: Overview
September 4, 2022
Installation
Getting Started
Via the plugins page Uploading via the WordPress Dashboard Using FTP
Read more ->
: Installation
September 4, 2022
WP Engine
Known Issues
WP Engine has a feature which prevents long queries from being executed. This is called the Long Query Governor. Unfortunately this feature often prevents our queries from executing correctly, either when building the indexer via wp-admin or when running our queries on the frontend of your site. You might see an error in your logs…
Read more ->
: WP Engine
October 17, 2024
Advanced Custom Fields (ACF)
Read more ->
: Advanced Custom Fields (ACF)
September 20, 2024
What’s new in version 3?
FAQs
Read more ->
: What’s new in version 3?
September 20, 2024
Advanced Custom Fields Overview
Advanced Custom Fields
Read more ->
: Advanced Custom Fields Overview
September 30, 2024
Queries Overview
Queries
Queries are the backbone of your site. From search, to blogs, to products listings and more, they power your website in many different ways. With Search & Filter, you can select the different queries across your site, choose to modify them, and attach fields such as search and filters to them (optional). The most important…
Read more ->
: Queries Overview
September 4, 2022
Queries
Developer
PHP Filter query args The query class: Search_Filter\Queries\Query The query instance class. Function: get_attributes() Description: Gets all the attributes for a query (most of the settings you can see in the query editor).Return: associative array of attributes.Use: $query->get_attributes() Function: get_attribute( $attribute_name ) Description: Gets a single attribute by name.Return: attribute value or null if attribute…
Read more ->
: Queries
September 27, 2024
Can I use my license on local or staging sites?
FAQs
Local sites and some supported staging sites will not count towards your activation limit. That means you can activate Search & Filter and receive updates on those sites regardless of your activation limit. Local sites We support local URLs that follow the following patterns: Staging sites We support stagings sites for the following hosts: We…
Read more ->
: Can I use my license on local or staging sites?
October 10, 2024
Fields Overview
Fields
Fields allow your visitors to interact with queries on your site, enabling them to drill down to find the information they are looking for. This means they spend less time looking for the information they need. Field types There are 5 different types of fields: Search, Choice, Range (pro), Advanced and Control. Search fields allow…
Read more ->
: Fields Overview
September 4, 2022

---

## WooCommerce Overview - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/woocommerce/woocommerce-overview/

Search & Filter has a deep integration with WooCommerce built in, all you need to do is enable it!
Enable the Integration
Head to
wp-admin
->
Search & Filter
->
Integrations
and ensure the WooCommerce integration is enabled.
WooCommerce Shop
Search & Filter supports both FSE and classic editor Shop pages.
To add filtering to your Shop ensure your query is set to
WooCommerce Shop
.
Checkout the full guide to
integrating with the WooCommerce Shop
.
Collections Block
WooCommerce Products Collections blocks can be placed on any page on your site to show product listings.
Learn how to setup Search & Filter with the Collections Block
(coming soon).
Products Shortcode
We also support filtering the WooCommerce Products shortcode –
[products]
.
Add the Query ID to the Shortcode
Add the
search_filter_query_id
attribute to your shortcode with your query ID to enable filtering the shortcode, where
123
is your query ID:
[products search_filter_query_id="123"]
Set the Query to use Products Shortcode
Supported Data Types
Search & Filter supports building filters with all your WooCommerce data:
Products + Variations Post Types
Product Categories
Product Tags
Product Brands (NEW)
Product Attributes
Stock Statuses
(Pro)
On Sale
(Pro)
When using the
Indexer
(Pro) feature Search & Filter intelligently searches your products and variations ensuring you only get results for combinations that actually exist!
On This Page
Enable the Integration
WooCommerce Shop
Collections Block
Products Shortcode
Add the Query ID to the Shortcode
Set the Query to use Products Shortcode
Supported Data Types
More From This Series
WooCommerce
WooCommerce Overview
WooCommerce Shop
WooCommerce Collections Block

---

## Live Search (Pro) - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/queries/live-search/

Settings
Live Search
Disable or enable the Live Search feature. When enabled, results will be updated without reloading the page. When disabled the page will reload.
Update URL
Updates the URL in the address bar to reflect the current search & filter state.
Fully supports the browser history API, meaning you can press backwards and forwards in the browser to instantly load previous results fields state.
Show Loading Icon
Enabled the loading icon spinner when fetching new results. This settings enable the
Loading Icon
tab with more configuration options.
Fade Results
Fades the results out when fetching new results. Fades them back in when the results have been fetched.
Results Container
Note:
this option may not be available. Some integration types handle this setting automatically for you.
A CSS selector to target the section on your site that that you want to be reloaded/updated when interacting with the search form – that contains your search results.
Choose a CSS selector that does not occur more than once on a page.
Examples could be:
#main
.search-results
Make sure that container chosen is wrapped around your
search results
(posts) and
pagination
.
Dynamic Sections
A CSS selector to target any other parts of the page to update.
For example, in addition to your results updating, you might also want to update the page title – then you would enter
h1
Note:
your CSS selector must target unique items on a page, if there are multiple instances of your selector on a page it will fail to update.
Scroll Window + Scroll To
One the results have updated you might want to scroll the window to particular section. Support options include:
Top
– scrolls the window all the way to the top of the page.
Query
– scrolls the window the
results container
, or the results list.
Field
– choose a connected field to scroll to.
Custom
– enter your own CSS selector to scroll to.
Pagination Type
Determines how your results will be paginated. Most queries use standard pagination but a
load more
pagination style is also available.
Normal
– using this setting assumes you will be using standard pagination, either numbers or prev/next links – this is the default option in WordPress and most plugins.
May reveal the setting
Pagination Selector
Load more
– use this option if you’d like to use a
Load More
button instead, which will reveal more results each time its pressed.
May reveal the setting
Posts Container
Make sure to add a
Load More
field underneath your results – you can do this by creating a
Control field
and setting the
Control Type
to
Load More
.
Pagination Selector
Note:
this option may not be available. Some integration types handle this setting automatically for you.
Only available when using
Normal Pagination
type.
Enter a CSS selector to target your pagination links, so results are also updated via Live Search when using them. The selector should target the anchor tag specifically, i.e.:
.pagination a
.pagination a.nav-links
Posts Container
Note:
this option may not be available. Some integration types handle this setting automatically for you.
Only available when using
Load More Pagination
type.
To use Load More funcitonality, it needs to know the exact container that contains only your individual posts / results, so that it may extract them and know where to place them.
Enter a CSS selector that container only your posts, where the direct child elements are the posts/results themselves.
On This Page
Settings
Live Search
Update URL
Show Loading Icon
Fade Results
Results Container
Dynamic Sections
Scroll Window + Scroll To
Pagination Type
Pagination Selector
Posts Container
More From This Series
Queries
Queries Overview
Query Editor
Live Search (Pro)
Results Shortcode (Pro)
Archives

---

## Advanced Custom Fields Overview - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/advanced-custom-fields/advanced-custom-fields-overview/

This article will be back up soon.
More From This Series
Advanced Custom Fields
Advanced Custom Fields Overview

---

## Beaver Builder - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/integrations/beaver-builder/

The
Search & Filter – Beaver Builder Extension
allows for seamless integration between Beaver Builder and Search & Filter.
With this extension, Search & Filter will now be able to directly integrate and filter the following Beaver Builder Modules:
Posts Module – including layout options Columns, Masonry, Gallery and List.
Posts Slider
Posts Carousel
WooCommerce
This includes support for
Beaver Themer
and archive locations.
Install + activate the extension
To get started first we need to enable the integration in our integrations screen.
Ensure you have
Beaver Builder
enabled.
Then from the Integrations screen, click
install extension
.
The extension plugin will be automatically downloaded in the background and then enabled.
If there are any issues downloading the extension, you can
download it from your account
and install it manually.
Create a query
Head to
Queries
in the main navigation, then press
Add New
to create a new query.
Ensure that location is set to
dynamic
and then choose
Beaver Builder Module
from the dropdown:
Give your query a
name
, hit
save
and your query is good to go.
There are a lot of settings
to fine tune your results.
Create a field
After saving your query, you’ll find your connected fields below. There won’t be any initially – press
Add New
to create one.
From here you can create as many fields as you need and connect them to the same query.
When creating fields for queries, ensure the
query integration
option is set to the correct query.
Read more about fields here
.
Adding fields to your site
Once you’ve created some fields, you can add them to your Beaver Builder powered site using the
Search & Filter Field
Module.
Note:
using shortcodes to place fields can lead to unexpected behaviour, it’s always best to use the Field Module.
Once you’ve added the module to your page you can choose the field you created earlier from the dropdown:
Filtering the Loop Module (new), Posts, Posts Slider & Posts Carousel Modules
To integrate with Beaver Builders Loop Module or one of the Posts Modules, first ensure that you’ve set the
Beaver Builder Module
option in your query
as described above
.
The next step is to connect your Loop/Posts Module to your Search & Filter query:
Head to the
Content
panel
Under
Source
, choose
Search & Filter
Then choose your query from the dropdown
Once connected Search & Filter is now ready to work with the Posts Module.
Filtering the WooCommerce Module
To integrate with any of the WooCommerce Module, first ensure that you’ve set the
Beaver Builder Module
option in your query
as described above
.
The next step is to connect your WooCommerce Module to your Search & Filter query:
From the layout dropdown, choose
Multiple Products
Under
Products Source
, choose
Search & Filter
Then choose your Search & Filter Query from the dropdown
Note:
you can also use the Posts Module to display WooCommerce Products, once you connect a query that uses WooCommerce Products, additional layout & styling options will be available.
Beaver Themer
Search & Filter will automatically integrate with archives built with Beaver Themer.
Usually for an Archive location you’ll want to use the
Posts Module
.
It’s recommended to set to set the
Content
->
Source
to use the
Main Query
:
When setting up an archive using the
Main Query
, the Search & Filter query must also be configured to use the archive query:
On This Page
Install + activate the extension
Create a query
Create a field
Adding fields to your site
Filtering the Loop Module (new), Posts, Posts Slider & Posts Carousel Modules
Filtering the WooCommerce Module
Beaver Themer
More From This Series
Integrations
Elementor
Beaver Builder
Relevanssi
GenerateBlocks
WPML
Polylang
Dynamic Content for Elementor
Easy Digital Downloads
Divi
WPBakery Page Builder

---

## Results Shortcode (Pro) - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/queries/results-shortcode/

With the shortcode setting, you can display your results anywhere on your site by using a shortcode – and then customise the results using PHP templates in your theme folder.
Enable Shortcodes
Head to the
Settings
screen and enable the
Shortcodes
setting.
By default they’re enabled already.
Create a Query
Set the location to
Dynamic
and the Integration to
Results Shortcode
.
Once you save the query, you’ll see a new option to copy the results shortcode.
Displaying the Results
Place this shortcode anywhere on your site to display the results from your query settings.
Create Connected Fields
Once you’ve saved your query, you can start creating and connecting fields below. iT Fields are optional, you can use queries solely for building listings without any fields at all.
Learn how to create and add fields to your query.
Customising the Results
By default, Search & Filter uses a predefined PHP template for displaying your query results.
This can be overriden in your theme. Search & Filter first looks in your theme folder for an appropriate template to use, and falls back to it’s own if there isn’t one.
Template Location
Templates should be stored in your theme folder, inside a sub folder called
search-filter
. The path should look like this:
./wp-content/themes/your-theme/
search-filter
/...
Where
your-theme
is the folder of your theme.
It is recommended to use a child theme
for customizations.
Create a Template With the ID of the Query
Search & Filter first checks the
search-filter
folder in your theme for a template matching your query ID. If your query ID is
123
then it would try to load the file:
./wp-content/themes/your-theme/
search-filter
/
123
.php
This allows you to create different results template for each of your queries.
Finding the Query ID
You can find the query ID at the top of the query edit screen:
It is also present in the results shortcode itself, where
123
would be the ID:
[searchandfilter query="
123
" action="show-results"]
Create a Fallback Template
If a template with your query ID is not found in your theme folder, then Search & Filter looks for a file called
results.php
in the same folder:
./wp-content/themes/your-theme/
search-filter
/
results
.php
This template will be used for any queries that don’t have their own specific template.
Copy the sample template
A good starting point is to use the template that comes with Search & Filter.
This can be found in:
./wp-content/plugins/search-filter-pro/includess/features/shortcodes/template.php
Copy this file to your theme folder and rename it to
results.php
– the path should be:
your-theme/search-filter/results.php
.
Once you’ve copied this over you’re ready to start customising the results.
Migrating from v2
If you’ve migrated from version 2 of Search & Filter there are a couple of things to note:
We no longer run
wp_reset_post_data()
automatically, it must be added to your template after the
$query->have_posts()
loop. It can be found on line
67
of the v3 template.
The container CSS class has changed to
.search-filter-query--id-123
(from
.search-filter-results-123
), where
123
is the query ID.
On This Page
Enable Shortcodes
Create a Query
Displaying the Results
Create Connected Fields
Customising the Results
Template Location
Create a Template With the ID of the Query
Create a Fallback Template
Copy the sample template
Migrating from v2
More From This Series
Queries
Queries Overview
Query Editor
Live Search (Pro)
Results Shortcode (Pro)
Archives

---

## Fields - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/developer/developer-fields/

PHP
The field class: Search_Filter\Fields\Field
The field instance class.
Function: get_attributes()
Description: Gets all the attributes for a query (most of the settings you can see in the query editor).
Return: associative array of attributes.
Use:
$query->get_attributes()
Function: get_attribute( $attribute_name )
Description: Gets a single attribute by name.
Return: attribute value or
null
if attribute not found.
Use:
$query->get_attribute('singleIntegration')
Function: get_id()
Description: Gets the field ID.
Return: the ID.
Use:
$field->get_id()
Function: get_values()
Description: Gets the field values.
Return: the ID.
Use:
$field->get_values()
Find a field
Returns:
Search_Filter\Fields\Field or a WP_Error if not found.
By name
$
field
=
\
Search_Filter
\
Fields
\
Field
::
find
(
array
(
'
name
'
=>
'
My field
'
,
// Field name
)
)
;
var_dump
(
$
field
)
;
By ID
$
field
=
\
Search_Filter
\
Fields
\
Field
::
find
(
array
(
'
id
'
=>
123
,
)
)
;
var_dump
(
$
field
)
;
Find multiple fields
Returns:
array of Search_Filter\Fields\Field
Find fields by status
$
queries
=
\
Search_Filter
\
Fields
::
find
(
array
(
'
status
'
=>
'
enabled
'
,
// Only get enabled fields.
'
number
'
=>
0
,
// Get all.
)
)
;
var_dump
(
$
queries
)
;
Get a fields active values
// Get the field by ID.
$
field
=
\
Search_Filter
\
Fields
\
Field
::
find
(
array
(
'
id
'
=>
123
,
// Replace 123 with your field ID.
)
)
;
// Get a field value(s)
var_dump
(
$
field
->
get_values
()
)
;
Modify a fields options
// Filter the choice options for a field and replace them with our own.
function
demo_filter_choice_options
(
$
options
,
$
field
)
{
$
field_id
=
$
field
->
get_id
()
;
// Ensure we only filter a field with the ID `123`.
if
(
$
field_id
!==
123
)
{
return
$
options
;
}
// We could instead check a field attribute, such as data type:
// $data_type = $field->get_attribute( 'dataType' );
// if ( $data_type !== 'my_custom_data_type' ) {
// return $options;
// }
/**
* Options can have:
* - label
* - value
* - count
* - depth
*
* Only value and label are required.
*/
$
custom_options
=
array
(
array
(
'
label
'
=>
'
Custom Option
'
,
'
value
'
=>
'
custom_option
'
,
'
count
'
=>
10
,
'
depth
'
=>
0
,
),
array
(
'
label
'
=>
'
Custom Option 2
'
,
'
value
'
=>
'
custom_option_2
'
,
'
count
'
=>
20
,
'
depth
'
=>
0
,
),
)
;
return
$
custom_options
;
}
add_filter
(
'
search-filter/field/choice/options
'
,
'
demo_filter_choice_options
'
,
10
,
2
)
;
Custom Data Types + Queries
Important
– this cannot be done from a theme, it must be run from a
custom plugin
.
Our hooks fire on
plugins_loaded
with a priority of
1
so the hooks must be setup before that, on a priority of
0
.
To create your own data type, first we need to add the data type to the
dataType
setting.
Create and add a custom data type
// Register custom data type.
function
demo_plugin_register_custom_data_type
()
{
// Add custom field option to data type setting.
$
data_type_setting
=
\
Search_Filter
\
Fields
\
Settings
::
get_setting
(
'
dataType
'
)
;
if
(
$
data_type_setting
)
{
$
custom_data_type
=
array
(
'
label
'
=>
__
(
'
My Custom Data Type
'
,
'
search-filter-pro
'
),
'
value
'
=>
'
my_custom_data_type
'
,
// Ensures its only displayed when an `Advanced` field type is selected
// Warning: this will change in an upcoming version.
'
dependsOn
'
=>
array
(
'
relation
'
=>
'
AND
'
,
'
rules
'
=>
array
(
array
(
'
option
'
=>
'
type
'
,
'
compare
'
=>
'
=
'
,
'
value
'
=>
'
advanced
'
,
),
),
),
)
;
$
data_type_setting
->
add_option
(
$
custom_data_type
)
;
}
}
// Add support for it for an input type.
add_action
(
'
search-filter/settings/register/fields
'
,
'
demo_plugin_register_custom_data_type
'
,
20
)
;
Add input type support for the data type
// Add support for it for an input type.
function
demo_plugin_add_custom_field_data_support
(
$
data_support
,
$
type
,
$
input_type
)
{
// Add the `my_custom_data_type` to the Advanced -> Date Picker field.
if
(
$
type
===
'
advanced
'
&&
$
input_type
===
'
date_picker
'
)
{
$
data_support
[]
=
array
(
'
dataType
'
=>
'
my_custom_data_type
'
,
)
;
}
return
$
data_support
;
}
add_filter
(
'
search-filter/field/get_data_support
'
,
'
demo_plugin_add_custom_field_data_support
'
,
20
,
3
)
;
Filter the WP_Query args based on the new field value
// Filter the query args based on the input type and data type.
function
demo_plugin_filter_field_query_args
(
$
query_args
,
$
field
)
{
// Return early if the field doesn't use our custom data type.
if
(
$
field
->
get_attribute
(
'
dataType
'
)
!==
'
my_custom_data_type
'
)
{
return
$
query_args
;
}
// Return early if the isn't the input type we wanted
if
(
$
field
->
get_attribute
(
'
inputType
'
)
!==
'
date_picker
'
)
{
return
$
query_args
;
}
// Now we have the custom data type, we can update the query args based on the field value.
// Use `get_value()` for fields that only need 1 value.
$
value
=
$
field
->
get_value
()
;
// Use `get_values()` for fields that have multiple values.
// $values = $field->get_values();
// If there is no value, bail.
if
(
empty
(
$
value
)
)
{
return
$
query_args
;
}
// Create a custom meta query based on the field value.
$
query_args
[
'
meta_query
'
]
=
array
(
array
(
'
key
'
=>
'
my_custom_meta_key
'
,
'
value
'
=>
$
value
,
'
compare
'
=>
'
>=
'
,
),
)
;
return
$
query_args
;
}
add_filter
(
'
search-filter/field/wp_query_args
'
,
'
demo_plugin_filter_field_query_args
'
,
20
,
2
)
;
JavaScript
Get an array of all fields on the page.
const
fields
=
window
.
searchAndFilter
.
frontend
.
fields
.
getAll
()
;
for
(
let
i
=
0
;
i
<
fields
.
length
;
i
++
)
{
const
field
=
fields
[
i
]
;
// Get the field ID.
console
.
log
(
field
.
getId
() )
;
// Get field attributes using getAttribute
console
.
log
(
field
.
getAttribute
(
'
type
'
) )
;
// search, choice, range, control
console
.
log
(
field
.
getAttribute
(
'
queryId
'
) )
;
// The connected query ID.
}
Get a single field by ID.
const
fieldId
=
123
;
// Replace `123` with your field ID.
const
field
=
window
.
searchAndFilter
.
frontend
.
fields
.
get
(
fieldId
)
;
if
(
field
)
{
// Get the query ID.
console
.
log
(
field
.
getId
() )
;
// Get query attributes using getAttribute
console
.
log
(
field
.
getAttribute
(
'
type
'
) )
;
// search, choice, range, control
console
.
log
(
field
.
getAttribute
(
'
queryId
'
) )
;
// The connected query ID.
}
On This Page
PHP
The field class: Search_Filter\Fields\Field
Find a field
Find multiple fields
Get a fields active values
Modify a fields options
Custom Data Types + Queries
JavaScript
Get an array of all fields on the page.
Get a single field by ID.
More From This Series
Developer
Queries
Fields
Theme Integration
Custom query integration
Changelogs

---

## Field Editor - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/fields/editor/

The field editor allows you to create, edit and design the frontend fields on your site.
Access the field editor via the Search & Filter
Dashboard
, then choose
Fields
in the main menu.
If you are using the
block editor
, you can access all the same settings and features directly via our block equivalents.
Name
When referencing the field throughout the site the name will be used.
It will not be visible on the frontend
It can be used in shortcodes (be careful when changing it though!)
Will be used when referencing the field in blocks and other frontend widgets and modules (for example, in an Elementor widget)
Type
This is where you can change the main field type.
Search
– allows for free text input to search for posts matching the search term.
Choice
– allows for a single selection or multiple selection from a set of options.
Range
– allow users to select a single numerical value within a specified range, or select two values to define a range to filter.
Advanced
– have more unique or complex functionality than the other field types.
Control
– interact with the query in different ways, such as submitting a search, resetting the fields, or changing the page of results
Learn more about field types.
Settings
This is where you will see a fully interactive preview of your field.
It will be populated by the data types you have chosen and will display any styling options you have applied.
Read more about field types
Styles
Clicking the styles tab will reveal a panel containing only styles settings. You can adjust design settings for the heading, description and input fields directly.
Design options include:
Multiple color options, for borders, background colors, hover colors and more.
Scale up and down your field sizes preserving padding and borders.
Paddings and margins
+ more coming soon!
Preview
This is where you will see a fully interactive preview of your field.
It will be populated by the data types you have chosen and will display any styling options you have applied.
Actions
You can save, update, or delete actions from the actions toolbar.
On This Page
Name
Type
Settings
Styles
Preview
Actions
More From This Series
Fields
Fields Overview
Field Editor
Field Types

---

## Elementor Extension - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/developer/changelogs/elementor-extension/

1.4.1
Improvement – add hardening to upgrade process.
Fix – issue with undefined array key
product_query_post_type
1.4.0
Improvment – rework integrations with widgets for better compatibility and stability with Search & Filter Version 3.
New – added “no results” message to the loop carousel.
New – support Elementor’s “load on click” and “infinite scroll” in Loop Grids.
New – support the Loop Grid “Individual Pagination” setting.
New – support “load more” pagination for portfolio widgets.
Fix – queries were sometimes not displayed in the Elementor editor.
Fix – JS errors when using the portfolio widget.
Fix – issues with live search when used on archives utilising the “current query” option.
Fix – re-added “no results” message to the products widget.
Fix – issues with WP 6.7 and load_text_domain.
1.3.4
Notice – ensure you are using the Search & Filter Elementor Field widgets for optimum compatibility (shortcodes are less stable).
Bump minumum Elementor version to 3.20.0.
Fix – issues with JavaScript initialisation with Search & Filter 3.
Fix – removed legacy “nothing found message” option from loop grids – Elementor has its own under ‘additional options’.
1.3.3
New – hook into the new integrations screen options and allow downloading from the dashboard.
Improvement – Reworked JS integration for more reliable behaviour.
Change – frontend JS filename changed from
search-filter-elementor.js
to
frontend.js
Fix – Support Search & Filter fields in Elementor popups.
Fix – Undefined PHP errors when accessing query attributes.
1.3.2
Fix – Error from Search & Filter 3.0.4 update.
1.3.1
Fix – Frontend JS errors.
1.3.0
New – add support for Search & Filter Pro v3
1.2.5
Fix – CSS issues when navigating from a page with no results.
Fix – an issue with the results class not being added to archive elementor widgets.
Fix – new JS errors after performing an ajax search.
Tested upto Elementor version 3.22
1.2.4
Tested upto Elementor version 3.19
1.2.3
Fix – issues with pagination & infinite scroll on the loop grid.
Fix – PHP warnings with the loop grid.
1.2.2
New – add support for product loop grid.
1.2.1
Fix – an issue with our search forms not working in popups since Elementor 3.9.0.
Fix – issues with deprecrated functions in Elementor.
1.2.0
Fix – Issue with deprecated _register_controls
Improvement – add message to widget that a search form needs to be selected.
New – add support for the Loop Grid widget.
1.0.10
Fix: Issue with the “no results” option not working in the Elementor posts widget.
1.0.9
Fix – add logo to search form widget
Fix – a JS issue when elementorFrontend isn’t loaded yet
Fix – remove no results message for Anywhere Elementor widgets (they provide their own)
New – add support for Anywhere Elementor Posts advanced
1.0.8
Fix – an undefined index error being thrown
Fix – a JS error relating the window not being declared properly when accessing
elementorFrontend
1.0.7
Improvement – register as a S&F extension to prevent conflicts
Fix – be more specific with the ajax pagination selector to prevent conflicts between instances
New – hooks to render custom content at the start/end of rendering (add content inside the ajax container)
1.0.6
Fix – an issue throwing a fatal error when using Elementor Free version only
New – add support for Anywhere Elementor Post Blocks
1.0.5
Fix – an issue with range sliders being duplicated in Elementor popups
Fix – remove some unnecessary error_log calls
1.0.4
Fix – a JS warning when editing a popup with our search form in
Fix – the “No Results” message was not working for the Product widget
1.0.3
New – Support search forms in popups
Fix – don’t assume Elementor is being used to build archives, check first before configuring settings
Fix – notice text when minimum PHP version is not met
Improvement – to workaround Polylang issues, we now show search forms for all languages in Elementor Widgets when Polylang is enabled
1.0.2
Fix – a PHP warning when no pagination was set
Fix – only re-init front end JS of elements we’ve updated – no more
elementorFrontend.init()
1.0.1
Remove some unused defines
Added in a missing
wp_reset_postdata()
1.0.0
Initial release
More From This Series
Developer
Queries
Fields
Theme Integration
Custom query integration
Changelogs

---

## Documentation - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/

Looking for an
integration
? Checkout the
integrations documentation
below.
Getting Started
Get to grips with basics and build your first search form.
Overview
Installation
Create a Query
Create a Field
Building a Layout
Queries
Find out what Queries are and how you can leverage them to build listings.
Queries Overview
Query Editor
Live Search (Pro)
Results Shortcode (Pro)
Archives
Fields
Learn about the different fields types and how to set them up.
Fields Overview
Field Editor
Field Types
Styles Presets
Learn how to create your own styles presets.
Styles Overview
Styles Editor
FAQ
Some of our most commonly asked questions.
What’s new in version 3?
Can I use my license on local or staging sites?
Debugging
Upgrading to Pro version 3 (from v2)
Troubleshooting
Block Editor
Learn how to create your fields & queries directly in the Block Editor.
Block Editor Overview
Block Editor – Add Fields
Block Editor – Create Queries
Developer
Documentation for advanced integrations & APIs.
Queries
Fields
Theme Integration
Custom query integration
Changelogs
Known Issues
Known issues with third party software and how to work around them.
WP Engine
WP Rocket
Integrations
Integrations
Find out the best way to get up and running using your favorite tools.
Elementor
Beaver Builder
Relevanssi
GenerateBlocks
WPML
Polylang
Dynamic Content for Elementor
Divi
WPBakery Page Builder
Easy Digital Downloads
WooCommerce
Get up an running with WooCommerce, however you use it.
WooCommerce Overview
WooCommerce Shop
WooCommerce Collections Block
Advanced Custom Fields
Learn how to power up your Search & Filter fields with ACF data.
Advanced Custom Fields Overview
Looking for version 2 documentation? Head to the
version 2 documentation site
.
Overview
Getting Started
Installation If you are familiar with WordPress, login to your site and search/install the Search & Filter plugin from the plugins page (once we’re out of beta). For more details, you can read our step by step installation instructions. The basics There are two main concepts that drive this plugin: Queries Queries are the backbone…
Read more ->
: Overview
September 4, 2022
Installation
Getting Started
Via the plugins page Uploading via the WordPress Dashboard Using FTP
Read more ->
: Installation
September 4, 2022
WP Engine
Known Issues
WP Engine has a feature which prevents long queries from being executed. This is called the Long Query Governor. Unfortunately this feature often prevents our queries from executing correctly, either when building the indexer via wp-admin or when running our queries on the frontend of your site. You might see an error in your logs…
Read more ->
: WP Engine
October 17, 2024
Advanced Custom Fields (ACF)
Read more ->
: Advanced Custom Fields (ACF)
September 20, 2024
What’s new in version 3?
FAQs
Read more ->
: What’s new in version 3?
September 20, 2024
Advanced Custom Fields Overview
Advanced Custom Fields
Read more ->
: Advanced Custom Fields Overview
September 30, 2024
Queries Overview
Queries
Queries are the backbone of your site. From search, to blogs, to products listings and more, they power your website in many different ways. With Search & Filter, you can select the different queries across your site, choose to modify them, and attach fields such as search and filters to them (optional). The most important…
Read more ->
: Queries Overview
September 4, 2022
Queries
Developer
PHP Filter query args The query class: Search_Filter\Queries\Query The query instance class. Function: get_attributes() Description: Gets all the attributes for a query (most of the settings you can see in the query editor).Return: associative array of attributes.Use: $query->get_attributes() Function: get_attribute( $attribute_name ) Description: Gets a single attribute by name.Return: attribute value or null if attribute…
Read more ->
: Queries
September 27, 2024
Can I use my license on local or staging sites?
FAQs
Local sites and some supported staging sites will not count towards your activation limit. That means you can activate Search & Filter and receive updates on those sites regardless of your activation limit. Local sites We support local URLs that follow the following patterns: Staging sites We support stagings sites for the following hosts: We…
Read more ->
: Can I use my license on local or staging sites?
October 10, 2024
Fields Overview
Fields
Fields allow your visitors to interact with queries on your site, enabling them to drill down to find the information they are looking for. This means they spend less time looking for the information they need. Field types There are 5 different types of fields: Search, Choice, Range (pro), Advanced and Control. Search fields allow…
Read more ->
: Fields Overview
September 4, 2022

---

## WP Engine - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/known-issues/wp-engine/

WP Engine has a feature which prevents long queries from being executed.
This is called the
Long Query Governor
.
Unfortunately this feature often prevents our queries from executing correctly, either when building the indexer via wp-admin or when running our queries on the frontend of your site.
You might see an error in your logs like this one:
KILLED QUERY (45767 characters long generated in /nas/content/live…
This means WP Engine’s long query governor stopped the query which can cause all kinds of issues when using our plugin.
Disabling the Long Query Governor
Fortunately there is an easy way to disable this feature – you will need to make a single code change to your site.
If you’re not comfortable making code changes to your site, please
open a ticket with WP Engine support
and ask them to do that for you, you can refer them to this article.
Step 1 – Edit
wp-config.php
Via SFTP, login to your site and locate the
wp-config.php
file in the root of your WordPress site, and edit it using a text editor.
Step 2 – Add a line of code to disable the long query governor
Near the bottom of the
wp-config.php
file you will find a line like this:
# That's It. Pencils down
Create a new line above, and add this line of code:
define( 'WPE_GOVERNOR', false );
It should then look like this:
define( 'WPE_GOVERNOR', false );
# That's It. Pencils down
Once you’ve done that and saved the file back to your server, the query governor is disabled allowing Search & Filter to work correctly.
You will need to rebuild the index from the Search & Filter dashboard once you’ve completed this step.
On This Page
KILLED QUERY (45767 characters long generated in /nas/content/live…
Disabling the Long Query Governor
Step 1 – Edit wp-config.php
Step 2 – Add a line of code to disable the long query governor
More From This Series
Known Issues
WP Engine
WP Rocket

---

## Search & Filter - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/developer/changelogs/search-filter/

3.1.6
Improvement – platform updates to support extensions.
Improvement – update integrations list.
Improvement – show ID column by default in admin.
3.1.5
Fix – an issue with rendering field previews in admin screens.
3.1.4
Fix – issue with the taxonomies tab not displaying correctly in the query editor.
Fix – issue when using past end of life database servers (MySQL version < 5.7 or MariaDB version < 10.2) when creating the options table.
Fix – error when queries are loaded in admin screens and trying to access
is_archive()
.
Fix – issue showing incorrect field counts in the query editor.
3.1.3
New – added hooks to support new pro features.
New – reworked WPML integration.
Improvement – logging and debugging tweaks.
Improvement – support publicly queryable post types in fields and queries.
Improvement – better performance in admins settings screens.
Improvement – better compatibility with the WooCommerce collections block.
Improvement – update license server URL.
Change – renamed the query and fields
remove()
function to
unload()
.
Fix – JavaScript issues in the block editor when using WooCommerce.
Fix – an issue detecting default post types to display.
Fix – an issue setting post types when using the Search location.
3.1.2
Improvement – stop using
getmypid()
when its not available (some hosting companies like Kinsta disable this function).
Fix – an issue with setting the correct post type for archives & WooCommerce shop.
Fix – issue with WooCommerce attributes that were not used for variations.
Fix – issue with the datepicker not clearing correctly after using a reset button.
Fix – number formatting issues when using the range slider.
Fix – show the “all options” default option as selected when no other options are selected.
Fix – an issue with the admin fields not rendering on a clean install.
3.1.1
New – added hooks to our rest api requests to prevent caching.
Fix – hotfix to remove the HPOS warning when using WooCommerce.
Fix – issues with field previews on new sites, when no queries have been created.
3.1.0
New – add support for WooCommerce Product Brands.
New – enable filtering on WooCommerce product archives option when using the shop integration.
New –
has_active_fields()
PHP method for queries.
New – added debugging options and logging levels.
Improvement – add plugin action link to the settings page.
Improvement – better detection of current page URL.
Improvement – add option values as data attributes for easier targetting with CSS.
Improvement – reliability with some hosts when generating our CSS file on the server.
Improvement – batch api requests in the block editor and admin screens.
Fix – a fatal error caused when using certain themes.
Fix – issues with WP 6.7 and loading translations too early.
Fix – an issue in the query editor when choosing taxonomy archives, causing the query tab to throw an error.
Fix – issues generating hierarchical taxonomy term URLs.
Fix – admin JS issues when navigating between templates in FSE.
Fix – styling issues with the sort fields label.
Fix – an issue with hierarchical taxonomies not showing posts only assigned to parents.
3.0.7
New – add notices to suggest enabling integrations when they are detected.
Change – remove beta feedback form.
Fix – select input types were not showing their placeholders on mobile and multiselect were not showing selections properly.
Fix – issues when using CSS variable colors from block editor themes.
Fix – an issue with the new query modal throwing an error in the block editor.
Fix – issues with the Main Query option not being available for archives.
Fix – stop enqueuing uncessary JS in admin screens.
3.0.6
New – New
dynamic
query integration location, replaces the dynamic toggle.
New – improvements to the integrations screen – install extensions with a single click!
New – Duplicate fields, queries & styles from the admin UI
Improvement – JavaScript APIs have been restructured and renamed.
Improvement – change the JS initialisation to improve compatibility.
Improvement – added ID column to admin tables – check the column view dropdown menu to enable it.
Improvement – disable text input on select fields on mobile devices.
Change – rename the query “integration” tab to to query “location”
Updated – renamed hooks in field render function to match naming conventions.
Fix – an issue with the count containers being added the DOM unnecessarily.
Fix – an admin error when shortcodes are disabled when using the fields dropdown.
Fix – issues with our fields not inheriting the block gap setting in the block editor.
Fix – order options in choice fields without case sensitivity.
3.0.5
Hotfix for fatal error thrown in Search & Filter Pro
3.0.4
New – added an “all items” option for radios, selects and buttons input type.
New – add limit depth, hide empty, show count, order by, include & exclude terms to WooCommerce data types.
Improvement – various admin UI improvements related to dynamically showing settings.
Improvement – set the default sticky posts option to ignore.
Fix – multiple issues with the UI showing out of date messaging in the block editor and admin screens.
Fix – limit number of options shown in fields wasn’t working on the frontend in some scenarios.
Fix – issue with fields when restricting taxonomy terms and post authors in the block editor.
Fix – indentation issues with hierarchical taxonomy checkboxes & radios.
Fix – order option in fields was not working when using post attributes as the data source.
Fix – counts were not showing in button fields.
Fix – issues with checkbox selection when pressing forwards/backwards in the browser history.
3.0.3
Fix – issues detecting the current page in a query.
Fix – properly respect relevance ordering if set in the query when a search term has been entered.
Fix – issues with Cron schedules.
Fix – issues with broken links.
3.0.2
New – add support to include/exclude taxonomy terms from fields.
New – added custom fields to query sort order.
New – added support for multiple sort orders to a query.
New – added sort order field type (control field).
Improvement – UI improvements to make working with shortcodes easier when the feature is enabled.
Fix – issues when integrations & features are updated and it not reflecting throughout the admin UI.
Fix – issues showing the correct styles in admin / block editor.
Fix – issue with connected queries and fields not displaying correctly in the admin list screens.
3.0.1
New – add sorting options for data types: post type, post status.
Improvement – show the ID of fields, queries & styles next to the screen title.
Fix – issues with fields not loading when block editor features are disabled.
Fix – an issue when changing field types and settings were persisting.
Fix – an issue with sort order not working correctly.
3.0.0
Fix – issue with placeholders sometimes not being the correct scale.
Fix – issue with buttons not applying the correct width.
Fix – issue with select dropdown positioning.
Fix – regression with archive queries not being properly attached.
Fix – issue with the button field not showing the selected option.
Fix – issues when migrating fields from older versions.
Fix – an JS issue being thrown with the ResizeObserver inside FSE iframes.
Fix – various issues when using taxonomy archive query integration.
Fix – issue with count brackets not showing.
3.0.0-beta-15
Platform upgrades to support the pro extension.
Minor bug fixes.
3.0.0-beta-14
Notice – updated the
search-filter/queries/query/apply_wp_query_args
hook to pass in the query object instead of the attributes.
Minor bug fixes.
Platform upgrades to support the pro extension.
3.0.0-beta-13
Fix – an issue with fields not submitting.
3.0.0-beta-12
New – revamped styles editor and block field styles.
New – added query option
Exclude Current Post
.
Changed – class names for fields, queries & styles
Tweak – added copy shortcode button for fields.
Fix – the wrong fields were showing when creating a new query.
Fix – various issues with taxonomy archives.
Fix – issues with pagination and the updated query block (also affects products block).
Fix – an issue where the plugin data was not removed, even though the setting to remove data on uninstall was enabled.
Notice – if you are using filters for post types and post stati via the block editor, these will need to be re-saved.
3.0.0-beta-11
Fix – an issue with checkbox filters throwing a PHP error
Fix – issues with taxonomy archive search not working correctly.
Fix – various JS issues with the site editor.
New – accessibility improvements.
New – enable post type archive queries to also filter taxonomy archives.
New – debugging tools
New – support for the site editor / FSE
3.0.0-beta-10
Fix – various admin layout issues due to an update in Gutenberg’s SlotFills system.
Improvement – rework the query editor in the block editor
Improvement – update the help screen
New – add integrations & settings pages
New – feedback widget for beta testers
New – add fallback support for legacy shortcodes
3.0.0-beta-9
Fix – issues with WP 6.4 and lodash no longer being loaded
3.0.0-beta-8
Fix – various issues with field previews in the styles editor
Fix – issues with the post type filter not working correctly
New – support hierarchical taxonomies in checkboxes, radios and select dropdowns
New – restrict hierarchical taxonomy depth
New – import/export styles
New – padding controls for fields
New – scale and spacing controls for labels
New – support extension of styles via themes
Improvement – various admin screen improvements including speed and caching
3.0.0-beta-7
Fix – an issue with the hide empty setting not working for taxonomies
Fix – an issue with our admin screens not loading when the WP install was in a subdirectory
Improvement – PHP 8.1 and 8.2 compatiblity
3.0.0-beta6
Fix – issue with some rest api requests preloading on the frontend
Fix – styling issues with WP 6.1
Fix – issue with query ID not working with query blocks
Updated – renamed our taxnomy comparison mode in filters
Updated – renamed woocommerce shop integration
Improved – support for the site editor
New – added query filter to fields admin screen
New – added breacrumbs to admin screens
New – Query editor sidebar for the block + site editor
New – reworked query editor for the Query Loop Block (you will need to reconnect your fields to query loops)
Notice
– please check the upgrade notes as you will need to reconfigure your saved queries with this update
3.0.0-beta-5
Add – a button to “go pro”.
Fix – pressing enter on the search input now submits the form.
Fix – an issue where entities were being double encoded.
Fix – an issue where the select dropdown auto-closed on mobile (when the on screen keyboard opens).
3.0.0-beta-4
Fix issue with shortcode implemenation where fields would not show their options.
3.0.0-beta-3
Update docs links
Update dashboard buttons
3.0.0-beta-2
Rename Template Field block to Reusable Field block –
breaking change
.
Add a context (reusable field / block editor fields) to fields admin page.
More From This Series
Developer
Queries
Fields
Theme Integration
Custom query integration
Changelogs

---

## Documentation - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/?query-0-page=2

Looking for an
integration
? Checkout the
integrations documentation
below.
Getting Started
Get to grips with basics and build your first search form.
Queries
Find out what Queries are and how you can leverage them to build listings.
Fields
Learn about the different fields types and how to set them up.
Styles Presets
Learn how to create your own styles presets.
FAQ
Some of our most commonly asked questions.
Block Editor
Learn how to create your fields & queries directly in the Block Editor.
Developer
Documentation for advanced integrations & APIs.
Known Issues
Known issues with third party software and how to work around them.
Integrations
Integrations
Find out the best way to get up and running using your favorite tools.
WooCommerce
Get up an running with WooCommerce, however you use it.
Advanced Custom Fields
Learn how to power up your Search & Filter fields with ACF data.
Looking for version 2 documentation? Head to the
version 2 documentation site
.
Block Editor Overview
Block Editor
Search & Filter comes with deep support and integration with all of core WordPress including the Block Editor, as standard. Field Blocks There are 6 field blocks available in the Block Editor: These blocks allow you to build your fields and queries directly in the Block Editor, ensuring you never break your workflow. Queries &…
Read more ->
: Block Editor Overview
May 31, 2025
Fields Overview
Fields
Fields allow your visitors to interact with queries on your site, enabling them to drill down to find the information they are looking for. This means they spend less time looking for the information they need. Field types There are 5 different types of fields: Search, Choice, Range (pro), Advanced and Control. Search fields allow…
Read more ->
: Fields Overview
September 4, 2022
WP Rocket
Known Issues
WP Rocket has a feature to delay JavaScript execution: Using this feature with Search & Filter can result in our search & filter fields not displaying at all. To work around this, we can add some rules to exclude our JavaScript files and objects. In the Excluded JavaScript Files section: Add the following rules (copy…
Read more ->
: WP Rocket
December 31, 2024
Queries
Developer
PHP Filter query args The query class: Search_Filter\Queries\Query The query instance class. Function: get_attributes() Description: Gets all the attributes for a query (most of the settings you can see in the query editor).Return: associative array of attributes.Use: $query->get_attributes() Function: get_attribute( $attribute_name ) Description: Gets a single attribute by name.Return: attribute value or null if attribute…
Read more ->
: Queries
September 27, 2024
Advanced Custom Fields Overview
Advanced Custom Fields
Read more ->
: Advanced Custom Fields Overview
September 30, 2024
WooCommerce Overview
WooCommerce
Search & Filter has a deep integration with WooCommerce built in, all you need to do is enable it! Enable the Integration Head to wp-admin -> Search & Filter -> Integrations and ensure the WooCommerce integration is enabled. WooCommerce Shop Search & Filter supports both FSE and classic editor Shop pages. To add filtering to…
Read more ->
: WooCommerce Overview
October 7, 2024
Query Editor
Queries
Name When referencing the query throughout the site the name will be used. Tabs Location Define how a Search & Filter query integrates with your site. Query Modify the query options to control what your users will see. Taxonomies Apply taxonomy restrictions to your queries, or exclude specific taxonomies or terms from your results. Post…
Read more ->
: Query Editor
December 17, 2023
Styles Overview
Styles
*Styling of fields has changed significantly. This section is being updated. The styles section allow you to define a styles preset to apply to your fields. For now this is limited to color choices only, in future this will incorperate fonts, borders, spacing, and possibly more. Creating custom styles This brings up the styles editor,…
Read more ->
: Styles Overview
September 4, 2022
Create a Field
Getting Started
After you have created your first query (link to the article), it’s time to get started with creating a field. While Search & Filter Queries are the backbone of the filtering and search functionality of our plugin, Fields allow your users to interact with the set options. There are various types of fields, but for…
Read more ->
: Create a Field
March 17, 2025
Field Editor
Fields
The field editor allows you to create, edit and design the frontend fields on your site. Access the field editor via the Search & Filter Dashboard, then choose Fields in the main menu. If you are using the block editor, you can access all the same settings and features directly via our block equivalents. Name…
Read more ->
: Field Editor
December 17, 2023

---

## Documentation – Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/block-editor/

Looking for an
integration
? Checkout the
integrations documentation
below.
Getting Started
Get to grips with basics and build your first search form.
Overview
Installation
Create a Query
Create a Field
Building a Layout
Queries
Find out what Queries are and how you can leverage them to build listings.
Queries Overview
Query Editor
Live Search (Pro)
Results Shortcode (Pro)
Archives
Fields
Learn about the different fields types and how to set them up.
Fields Overview
Field Editor
Field Types
Styles Presets
Learn how to create your own styles presets.
Styles Overview
Styles Editor
FAQ
Some of our most commonly asked questions.
What’s new in version 3?
Can I use my license on local or staging sites?
Debugging
Upgrading to Pro version 3 (from v2)
Troubleshooting
Block Editor
Learn how to create your fields & queries directly in the Block Editor.
Block Editor Overview
Block Editor – Add Fields
Block Editor – Create Queries
Developer
Documentation for advanced integrations & APIs.
Queries
Fields
Theme Integration
Custom query integration
Changelogs
Known Issues
Known issues with third party software and how to work around them.
WP Engine
WP Rocket
Integrations
Integrations
Find out the best way to get up and running using your favorite tools.
Elementor
Beaver Builder
Relevanssi
WPML
GenerateBlocks
Polylang
Dynamic Content for Elementor
Easy Digital Downloads
Divi
WPBakery Page Builder
WooCommerce
Get up an running with WooCommerce, however you use it.
WooCommerce Overview
WooCommerce Shop
WooCommerce Collections Block
Advanced Custom Fields
Learn how to power up your Search & Filter fields with ACF data.
Advanced Custom Fields Overview
Looking for version 2 documentation? Head to the
version 2 documentation site
.
Block Editor Overview
Block Editor
Search & Filter comes with deep support and integration with all of core WordPress including the Block Editor, as standard. Field Blocks There are 6 field blocks available in the Block Editor: These blocks allow you to build your fields and queries directly in the Block Editor, ensuring you never break your workflow. Queries &…
Read more ->
: Block Editor Overview
May 31, 2025
Block Editor – Add Fields
Block Editor
Getting started with the Search & Filter in the Block Editor couldn’t be easier, choose from 5 types of fields to add as well as the re-usable field block. There are 5 field types, each with their own block: Search, Choice, Range (Pro), Advanced and Control. To get started, open the block inserter and search…
Read more ->
: Block Editor – Add Fields
May 31, 2025
Block Editor – Create Queries
Block Editor
Creating Search & Filter Queries How it Works Search & Filter comes with its own advanced query editor – acting as a bridge between results listings and our fields. To connect a field to a query, we need to: Creating Queries While it is possible to create queries & fields via our admin pages, everything…
Read more ->
: Block Editor – Create Queries
June 1, 2025

---

## Documentation – Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/styles/

Looking for an
integration
? Checkout the
integrations documentation
below.
Getting Started
Get to grips with basics and build your first search form.
Overview
Installation
Create a Query
Create a Field
Building a Layout
Queries
Find out what Queries are and how you can leverage them to build listings.
Queries Overview
Query Editor
Live Search (Pro)
Results Shortcode (Pro)
Archives
Fields
Learn about the different fields types and how to set them up.
Fields Overview
Field Editor
Field Types
Styles Presets
Learn how to create your own styles presets.
Styles Overview
Styles Editor
FAQ
Some of our most commonly asked questions.
What’s new in version 3?
Can I use my license on local or staging sites?
Debugging
Upgrading to Pro version 3 (from v2)
Troubleshooting
Block Editor
Learn how to create your fields & queries directly in the Block Editor.
Block Editor Overview
Block Editor – Add Fields
Block Editor – Create Queries
Developer
Documentation for advanced integrations & APIs.
Queries
Fields
Theme Integration
Custom query integration
Changelogs
Known Issues
Known issues with third party software and how to work around them.
WP Engine
WP Rocket
Integrations
Integrations
Find out the best way to get up and running using your favorite tools.
Elementor
Beaver Builder
Relevanssi
WPML
GenerateBlocks
Polylang
Dynamic Content for Elementor
Easy Digital Downloads
Divi
WPBakery Page Builder
WooCommerce
Get up an running with WooCommerce, however you use it.
WooCommerce Overview
WooCommerce Shop
WooCommerce Collections Block
Advanced Custom Fields
Learn how to power up your Search & Filter fields with ACF data.
Advanced Custom Fields Overview
Looking for version 2 documentation? Head to the
version 2 documentation site
.
Styles Overview
Styles
*Styling of fields has changed significantly. This section is being updated. The styles section allow you to define a styles preset to apply to your fields. For now this is limited to color choices only, in future this will incorperate fonts, borders, spacing, and possibly more. Creating custom styles This brings up the styles editor,…
Read more ->
: Styles Overview
September 4, 2022
Styles Editor
Styles
Read more ->
: Styles Editor
December 17, 2023

---

## Debugging - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/faqs/debugging/

To access your data for debugging follow these steps:
Enable debugging tools
Head to the Search & Filter settings screen, and
enable
the
debugging tools
.
Export Data
Head to the
page with your query and filters
and click the Search & Filter
admin bar
menu item to open the sidebar.
At the bottom of the sidebar is an export data button. This will download a JSON file with your configuration.
It does contain your URL, query and filter setup, and some basic information about the current page.
On This Page
Enable debugging tools
Export Data
More From This Series
FAQs
What’s new in version 3?
Can I use my license on local or staging sites?
Debugging
Upgrading to Pro version 3 (from v2)
Troubleshooting

---

## Can I use my license on local or staging sites? - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/faqs/can-i-use-my-license-on-local-or-staging-sites/

Local sites and some supported staging sites
will not count towards your activation limit
.
That means you can activate Search & Filter and receive updates on those sites regardless of your activation limit.
Local sites
We support local URLs that follow the following patterns:
localhost
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
*.dev
*.local
*.test
Staging sites
We support stagings sites for the following hosts:
WP Engine
InstaWP
Cloudways
Kinsta
GoDaddy
FlyWheel
BlueHost
HostGator
SiteGround
We also support staging sites with the following patterns:
*.staging.example.org
*.test.example.org
staging-*.example.org
dev.example.org
On This Page
Local sites
Staging sites
More From This Series
FAQs
What’s new in version 3?
Can I use my license on local or staging sites?
Debugging
Upgrading to Pro version 3 (from v2)
Troubleshooting

---

## Beaver Builder Extension - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/developer/changelogs/beaver-builder-extension/

1.4.1
Hotfix – prevent an incorrect check for a newer version of Search & Filter.
1.4.0
New – add support for filtering the new loop module in Beaver Themer with Search & Filter v3.
Improvement – Compatibility updates for Beaver Builder 2.1
Improvement – compatiblity updates for Search & Filter 3.2.0.
1.3.0
Improvement – rework integrations with modules for better compatibility and stability with Search & Filter Version 3.
New – fully support all post module layouts – columns, masonry, gallery and list.
New – add support for all pagination types across all supported modules & layouts.
New – added support for Beaver Themer’s WooCommerce options in the post module.
Fix – issues with Beaver Themer and archives.
Fix – issue with the WooCommerce module showing products under the wrong conditions.
Fix – issues with Masonry and re-initialising layouts after a search.
Fix – inconsistencies with pagination.
1.2.5
Update supported version to support the lastest version of Search & Filter v3.
1.2.4
New – hook into the new integrations screen options and allow downloading from the dashboard.
New – add load more button support for pagination.
1.2.3
Fix – issue with the plugin not loading in conjuction with Search & Filter v2.
1.2.2
Hotfix – bypass critical error.
1.2.2
Hotfix – bypass critical error.
1.2.1
Update – change hooks to support Search & Filter 3.0.4.
1.2.0
New – add support for Search & Filter Pro v3
New – add support for WooCommerce multiple products module type (S&F v3 only).
1.0.1
Fix – Stop using
the_post()
and
wp_reset_postdata()
to loop through some of our queries – causes some very strange bugs
Fix – an issue with “equal heights” option not being respected in BB Module settings
Fix – an issue with our JS not firing when BB Posts Module Layout is set to “Columns”
New – add support for BB pagination types: Numbers, Scroll, Load More
New – add support for Gallery layout in Post Module
1.0.0
Init release
More From This Series
Developer
Queries
Fields
Theme Integration
Custom query integration
Changelogs

---

## Query Editor - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/queries/query-editor/

Name
When referencing the query throughout the site the name will be used.
It will not be visible on the frontend
It will be used when referencing queries in the block editor and other areas of the site such as in our various page builder widgets, for example, in our Elementor field widget
Tabs
Location
Define how a Search & Filter query integrates with your site.
Query
Modify the query options to control what your users will see.
Taxonomies
Apply taxonomy restrictions to your queries, or exclude specific taxonomies or terms from your results.
Post Meta (Pro)
Build complex post meta queries to refine your results.
Note:
post meta queries can cause overheads, use sparingly especially with high volumes of posts.
Live Search(Pro)
Reload results without refreshing your page. With multiple configuration options to get you up and running.
Loading Icon (Pro)
Customise the loading icon when using the Live Search feature. Change options such as size, color, borders background color, padding, margin and position.
Connected Fields
Once you’ve saved your query, the connected fields section appears.
Use this as a way to create fields and manage fields associated with the current query.
On This Page
Name
Tabs
Location
Query
Taxonomies
Post Meta (Pro)
Live Search(Pro)
Loading Icon (Pro)
Connected Fields
More From This Series
Queries
Queries Overview
Query Editor
Live Search (Pro)
Results Shortcode (Pro)
Archives

---

## Block Editor - Add Fields - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/block-editor/block-editor-add-fields/

Getting started with the Search & Filter in the Block Editor couldn’t be easier, choose from 5 types of fields to add as well as the re-usable field block.
There are 5 field types, each with their own block:
Search
,
Choice
,
Range
(Pro),
Advanced
and
Control
.
To get started, open the block inserter and search for the block name or scroll to the
Search & Filter
section.
Create a Field
Add the
Search Field
block to the page.
Query Integration
This is one of the most important options for any field, this is where you can define which query a field is supposed to affect.
When you first start using Search & Filter you’ll see the message “No queries found, create a query” – clicking
create a query
will open our query editor modal.
A query (results listing) can be on the current page, or somewhere else completely – use the query editor to configure the location and query parameters.
Learn How to Create Queries in the Block Editor
Once you’ve created your first query you will be able to choose it from the dropdown:
Field Settings
Once you’ve added your block to the page and setup the connected query you can start configuring your field.
There are common options between field types, as well as some unique options that are specific to each field type.
Common Options
Input Type
The type of input field used to for the field. For
search
fields, this could be
text
or
autocomplete
, and for
choice
fields this could be
select
,
radio
or
button
(there are more options).
Data Type
This setting (and its sub settings) allow you to choose what data source the field is connected to.
For a
choice
field, you could generate the options from a taxonomy or custom field.
URL Name (Pro)
Customise the URL name for the field – if you entered
search-value
then the URL would look like:
yoursite.com/?
search-value
=...
Label & Description
Adds a label or description above the field. This needs to be filled in with a relevant label even if you don’t show the label as this is what screen readers will use when it is visually hidden.
Auto Submit (Pro)
Enabling auto submit submits the search or filter field after any user interaction – removing the need for a separate submit button. A delay can be defined to allow a user more time to make changes to the field before the submit is triggered.
Default Value (Pro)
A default value can be set for the field so that it is preselected for your users. Depending on context, it could be dynamically generated ie:
If the field uses the
category taxonomy
as the
data type
and was displayed on a category archive, the field could then set the current taxonomy archive location as its default value.
Unique Options
Each field type (search, choice, range, advanced, control) has its own set of options, which can be customised and may reveal further options as you make selections.
There are many settings that are related to the
input type,
depending on your choice of input type you will be presented with further customisation options.
Styles Tab
The styles tab can be used to override and customise the styles of any field type.
Initially your fields will be displayed using the default styles preset. Use the dropdowns to add overrides and customise the design on a per field basis.
Once you’ve added the overrides you can customise them further:
Creating Presets
While styles can be overridden on an individual block basis, its also possible to create your own presets.
This allows you to create a preset to work across all your fields, providing a consistent design and preventing repetition when building your fields, as well as allowing you to update the styles of all your fields with one-click by setting the default.
Learn How to Create Styles Presets
On This Page
Create a Field
Query Integration
Field Settings
Common Options
Unique Options
Styles Tab
Creating Presets
More From This Series
Block Editor
Block Editor Overview
Block Editor – Add Fields
Block Editor – Create Queries

---

## Changelogs - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/developer/changelogs/

Below are the changelogs for the Search & Filter plugins and their extensions.
Search & Filter
Search & Filter Pro
Search & Filter – Elementor Extension
Search & Filter – Beaver Builder Extension
Search & Filter – WPML Extension
Search & Filter – GenerateBlocks Extension
More From This Series
Developer
Queries
Fields
Theme Integration
Custom query integration
Changelogs

---

## Divi - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/integrations/divi/

The Divi integration is not quite ready for Search & Filter Version 3 – but we’re working on it!
Checkout the version 2 documentation here.
More From This Series
Integrations
Elementor
Beaver Builder
Relevanssi
GenerateBlocks
WPML
Polylang
Dynamic Content for Elementor
Easy Digital Downloads
Divi
WPBakery Page Builder

---

## Custom query integration - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/developer/custom-query-integration/

Creating a custom query integration requries several steps depending on your needs.
Setting up your query
To connect Search & Filter with your query you will need to add an argument to the query itself with the name
search_filter_query_id
. The value of this argument should be the ID of of the Search & Filter query you want to connect to.
Adding as an argument
When creating a query the argument can be passed in just like the other arguments:
$
args
=
array
(
'
post_type
'
=>
array
(
'
post
'
),
'
search_filter_query_id
'
=>
1
,
'
paged
'
=>
get_query_var
(
'
paged
'
)
?
get_query_var
(
'
paged
'
)
:
1
,
)
;
$
query
=
new
WP_Query
(
$
args
)
;
Modifying an existing query
To modify an existing query you would need to use the
pre_get_posts
hook, from here you need to call
set()
on the query and add the
search_filter_query_id
argument.
function
pre_get_posts_function
(
$
query
)
{
$
query
->
set
(
'
search_filter_query_id
'
,
1
)
;
}
add_action
(
'
pre_get_posts
'
,
array
(
$this
,
'
pre_get_posts_function
'
)
)
;
Warning: pagination issues with
get_posts
The WordPress function for creating posts via
get_posts
automatically sets the argument
no_found_rows
to
true
.
This means the query will not return pagination information preventing
pagination
and
load more
functionality from working correctly.
For this reason it is generally preffered to instantiate a new
WP_Query
ie:
$query = new WP_Query( $args );
Adding the query integration to admin
The next step is to add a new option in our UI allowing users to select this new query integration.
This can be done using the
search-filter/settings/init
hook:
add_action
(
'
search-filter/settings/init
'
,
'
example_add_integration_option
'
),
10
)
;
/**
* Add a new query integration option - 'Custom query widget' to the list of
* single integration options.
*/
function
example_add_integration_option
()
{
// Get the setting.
$
query_integration_setting
=
\
Search_Filter
\
Queries
\
Settings
::
get_setting
(
'
queryIntegration
'
)
;
if
(
!
$
query_integration_setting
)
{
return;
}
$
new_integration_type_option
=
array
(
'
label
'
=>
__
(
'
Custom query widget
'
,
'
search-filter
'
),
'
value
'
=>
'
vendor-prefix/widget-name
'
,
)
;
$
query_integration_setting
->
add_option
(
$
new_integration_type_option
)
;
}
This adds the option to the query options dropdown:
Note:
vendor-prefix/widget-name
should be changed – this is used internally as a reference.
Once this step is complete the query integration should already be working.
Supporting dynamic update
Search & Filter Pro supports dynamic updating of the results – this means the results will be updated without refreshing the page.
To support this there are two steps:
Add the CSS selectors for the query
We can use the
search-filter/queries/query/get_attributes
filter to overide the query settings and insert our own
queryContainer
and
queryPaginationSelector
values.
add_filter
(
'
search-filter/queries/query/get_attributes
'
,
'
example_update_query_attributes
'
,
10
,
2
)
;
/**
* Automatically set the Ajax CSS selectors for the query container and pagination
* so the user doesn't have to set it themselves.
*/
function
example_update_query_attributes
(
$
attributes
,
$
query
)
{
// We want `queryContainer` and `queryPaginationSelector` to be set automatically.
$
id
=
$
query
->
get_id
()
;
if
(
!
isset
(
$
attributes
[
'
queryIntegration
'
]
)
)
{
return
$
attributes
;
}
$
query_integration
=
$
attributes
[
'
queryIntegration
'
]
;
if
(
$
query_integration
===
'
vendor-prefix/widget-name
'
)
{
// The query container is a CSS selector that contains the results and pagination.
$
attributes
[
'
queryContainer
'
]
=
'
.my-custom-query
'
;
// The pagination selector must be considered a child of the query container.
// An attribute of `.pagination a` will be converted to `.my-custom-query .pagination a`.
$
attributes
[
'
queryPaginationSelector
'
]
=
'
.pagination a
'
;
}
return
$
attributes
;
}
Note:
as there can be multiple queries on a page its best if this class or ID is unique, internally we use the query ID as the class name to ensure uniqueness.
Note 2:
'vendor-prefix/widget-name'
needs to be updated to reflect your reference name.
Hide the CSS selector options from the UI
Warning: this implementation is likely to change
.
Again we can use the register hook to modify the options and change the conditions to display these settings.
add_action
(
'
search-filter/settings/init
'
,
array
(
$this
,
'
example_hide_css_selector_options
'
),
10
)
;
/**
* Hide the query container and pagination selector settings from the user as we're
* automatically setting them above.
*/
public
function
example_hide_css_selector_options
()
{
$
depends_conditions
=
array
(
'
relation
'
=>
'
AND
'
,
'
action
'
=>
'
hide
'
,
'
rules
'
=>
array
(
array
(
'
option
'
=>
'
queryIntegration
'
,
'
compare
'
=>
'
!=
'
,
'
value
'
=>
'
vendor-prefix/widget-name
'
,
),
),
)
;
$
query_container
=
\
Search_Filter
\
Queries
\
Settings
::
get_setting
(
'
queryContainer
'
)
;
if
(
$
query_container
)
{
$
query_container
->
add_depends_condition
(
$
depends_conditions
)
;
}
$
pagination_selector
=
\
Search_Filter
\
Queries
\
Settings
::
get_setting
(
'
queryPaginationSelector
'
)
;
if
(
$
pagination_selector
)
{
$
pagination_selector
->
add_depends_condition
(
$
depends_conditions
)
;
}
// To support "load more".
$
query_posts_container
=
\
Search_Filter
\
Queries
\
Settings
::
get_setting
(
'
queryPostsContainer
'
)
;
if
(
$
query_posts_container
)
{
$
query_posts_container
->
add_depends_condition
(
$
depends_conditions
)
;
}
}
Essentially, this code specifies that the setting should only be displayed if the integration type is set to a single page and the single integration type is not set to the integration name.
Note:
vendor-prefix/widget-name
needs to be updated with the name you have chosen.
Once these steps have been completed your query should support all Search & Filter features.
Example plugin
You can use our example plugin as a guide, it uses a shortcode to create a custom query listing and then configures the options above to support dynamic updates.
Download example plugin (currently unavailable)
* Download will be available again when we launch the new site.
Use the shortcode
[my_custom_query]
to display the query.
Allowing users to choose a query
If you are building a query or widget that will be distributed, it is often a good idea to allow a user to choose which Search & Filter query they would like to connect to your widget.
To get a list of Search & Filter queries to choose from you can use the following code:
$
queries
=
\
Search_Filter
\
Queries
::
find
(
array
(
'
status
'
=>
'
enabled
'
,
// Only get enabled queries.
'
number
'
=>
0
,
// Get all.
'
meta_query
'
=>
array
(
array
(
'
key
'
=>
'
query_integration
'
,
'
value
'
=>
'
vendor-prefix/widget-name
'
,
'
compare
'
=>
'
=
'
,
),
),
),
'
records
'
)
;
var_dump
(
$
queries
)
;
Note:
here we will fetch a list of queries that have specifically been set to use
vendor-prefix/widget-name
On This Page
Setting up your query
Adding as an argument
Modifying an existing query
Warning: pagination issues with get_posts
Adding the query integration to admin
Supporting dynamic update
Add the CSS selectors for the query
Hide the CSS selector options from the UI
Example plugin
Allowing users to choose a query
More From This Series
Developer
Queries
Fields
Theme Integration
Custom query integration
Changelogs

---

## Documentation - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/?query-0-page=3

Looking for an
integration
? Checkout the
integrations documentation
below.
Getting Started
Get to grips with basics and build your first search form.
Queries
Find out what Queries are and how you can leverage them to build listings.
Fields
Learn about the different fields types and how to set them up.
Styles Presets
Learn how to create your own styles presets.
FAQ
Some of our most commonly asked questions.
Block Editor
Learn how to create your fields & queries directly in the Block Editor.
Developer
Documentation for advanced integrations & APIs.
Known Issues
Known issues with third party software and how to work around them.
Integrations
Integrations
Find out the best way to get up and running using your favorite tools.
WooCommerce
Get up an running with WooCommerce, however you use it.
Advanced Custom Fields
Learn how to power up your Search & Filter fields with ACF data.
Looking for version 2 documentation? Head to the
version 2 documentation site
.
WooCommerce Overview
WooCommerce
Search & Filter has a deep integration with WooCommerce built in, all you need to do is enable it! Enable the Integration Head to wp-admin -> Search & Filter -> Integrations and ensure the WooCommerce integration is enabled. WooCommerce Shop Search & Filter supports both FSE and classic editor Shop pages. To add filtering to…
Read more ->
: WooCommerce Overview
October 7, 2024
Search & Filter Pro
Developer
Read more ->
: Search & Filter Pro
January 11, 2025
WooCommerce Collections Block
WooCommerce
The first step is to ensure our WooCommerce integration is enabled. Enable the Integration Head to wp-admin -> Search & Filter -> Integrations and ensure the WooCommerce integration is enabled. Create a Page with the Collections Block Add a Product Collection block from the Block Inserter and then choose Create Your Own: To link our…
Read more ->
: WooCommerce Collections Block
March 17, 2025
Field Types
Fields
There are 5 different types of fields: Search, Choice, Range, Advanced and Control. Search Fields Search fields allow for free text input to search for posts matching the search term. Input types include: Choice Fields Choice fields allow for a single selection or multiple selection from a set of options. Input types include: Coming soon:…
Read more ->
: Field Types
September 5, 2022
Elementor
Integrations
The Search & Filter – Elementor Extension allows for seamless integration between Elementor and Search & Filter. With this extension, Search & Filter will now be able to directly integrate and filter the following Elementor widgets: Install + activate the extension To get started first we need to enable the integration in our integrations screen.…
Read more ->
: Elementor
September 30, 2024
Styles Editor
Styles
Read more ->
: Styles Editor
December 17, 2023
Live Search (Pro)
Queries
Settings Live Search Disable or enable the Live Search feature. When enabled, results will be updated without reloading the page. When disabled the page will reload. Update URL Updates the URL in the address bar to reflect the current search & filter state. Fully supports the browser history API, meaning you can press backwards and…
Read more ->
: Live Search (Pro)
October 15, 2024
WooCommerce Shop
WooCommerce
The first step is to ensure our WooCommerce integration is enabled. Enable the Integration Head to wp-admin -> Search & Filter -> Integrations and ensure the WooCommerce integration is enabled. Create a Query To link our fields with the WooCommerce Shop query, we need to create a query integration. Head to wp-admin -> Search &…
Read more ->
: WooCommerce Shop
September 20, 2024
Block Editor – Create Queries
Block Editor
Creating Search & Filter Queries How it Works Search & Filter comes with its own advanced query editor – acting as a bridge between results listings and our fields. To connect a field to a query, we need to: Creating Queries While it is possible to create queries & fields via our admin pages, everything…
Read more ->
: Block Editor – Create Queries
June 1, 2025
Fields
Developer
PHP The field class: Search_Filter\Fields\Field The field instance class. Function: get_attributes() Description: Gets all the attributes for a query (most of the settings you can see in the query editor).Return: associative array of attributes.Use: $query->get_attributes() Function: get_attribute( $attribute_name ) Description: Gets a single attribute by name.Return: attribute value or null if attribute not found.Use: $query->get_attribute(‘singleIntegration’)…
Read more ->
: Fields
November 26, 2024

---

## WP Rocket - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/known-issues/wp-rocket/

WP Rocket has a feature to delay JavaScript execution:
Using this feature with Search & Filter can result in our search & filter fields not displaying at all.
To work around this, we can add some rules to exclude our JavaScript files and objects.
In the
Excluded JavaScript Files
section:
Add the following rules (copy & paste):
/wp-content/plugins/search-filter-pro/assets/js/frontend/frontend.js
/wp-content/plugins/search-filter/assets/js/frontend/frontend.js
/wp-content/plugins/search-filter-elementor/assets/v3/js/frontend.js
/wp-content/plugins/search-filter/assets/js/vendor/flatpickr.js
window.searchAndFilter
window.searchAndFilterData
window.searchAndFilterApiUrl
/
wp
-
content
/
plugins
/
search
-
filter
-
pro
/
assets
/
js
/
frontend
/
frontend
.
js
/
wp
-
content
/
plugins
/
search
-
filter
/
assets
/
js
/
frontend
/
frontend
.
js
/
wp
-
content
/
plugins
/
search
-
filter
-
elementor
/
assets
/
v3
/
js
/
frontend
.
js
/
wp
-
content
/
plugins
/
search
-
filter
/
assets
/
js
/
vendor
/
flatpickr
.
js
window
.
searchAndFilter
window
.
searchAndFilterData
window
.
searchAndFilterApiUrl
Once they’ve been added and saved, Search & Filter should work again as normal.
More From This Series
Known Issues
WP Engine
WP Rocket

---

## WPML - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/integrations/wpml/

Both Search & Filter Pro and the Base (free) version integrate with WPML via our
Search & Filter – WPML Extension
plugin – allowing you translate your search & filter fields and search for content in any language!
Get the Extension
Via the Pro Plugin
Enable the extension by heading to
wp-admin
->
Search & Filter
->
Integrations
and then using the toggle to enable the extension – this will automatically install and activate the extension for you.
Via the Base Plugin
Download the WPML Extension Plugin
, upload it to your site and then activate the plugin from the plugins dashboard.
Translating Fields
Whenever a field is created or updated, it is added to WPMLs translation management screen.
You can filter the translation management screen by
Search & Filter Field
to see all your fields at once.
Once you’ve selected which Fields you want to translate, you can add them to the translation queue.
Adding Existing Fields
When you first setup WPML your existing Search & Filter Fields won’t be recognised by WPML until you save them.
Quickly and easily import your existing fields using the
Add Existing Fields to Translation Management
feature.
Head to
wp-admin
->
Search & Filter
->
Integrations
->
WPML
Then select the settings icon:
And click the
Add Existing Fields
button:
Once the process is complete, all your existing fields will be available in WPMLs translation management.
WooCommerce Multilingual
The
WooCommerce Multilingual Plugin
is required to translate your WooCommerce products, variations, categories, tags and attributes.
Search & Filter fully supports the WooCommerce Multilingual Plugin.
ACF Multilingual
To translate Advanced Custom Fields you will need to install the
ACF ML plugin from WPML
.
Search & Filter Pro currently supports some features of ACF ML, we’re working on improving this integration.
On This Page
Get the Extension
Via the Pro Plugin
Via the Base Plugin
Translating Fields
Adding Existing Fields
WooCommerce Multilingual
ACF Multilingual
More From This Series
Integrations
Elementor
Beaver Builder
Relevanssi
GenerateBlocks
WPML
Polylang
Dynamic Content for Elementor
Easy Digital Downloads
Divi
WPBakery Page Builder

---

## WPBakery Page Builder - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/integrations/wpbakery-page-builder/

The WPBakery Page Builder integration is not quite ready for Search & Filter Version 3 – but we’re working on it!
Checkout the version 2 documentation here.
More From This Series
Integrations
Elementor
Beaver Builder
Relevanssi
GenerateBlocks
WPML
Polylang
Dynamic Content for Elementor
Easy Digital Downloads
Divi
WPBakery Page Builder

---

## Queries - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/developer/developer-queries/

PHP
Filter query args
add_action
(
'
search-filter/query/query_args
'
,
'
search_filter_docs_update_query_args
'
,
10
,
2
)
;
function
search_filter_docs_update_query_args
(
$
query_args
,
$
search_filter_query
)
{
// Get the query ID.
$
query_id
=
$
search_filter_query
->
get_id
()
;
// If the query ID is 123, update the order.
if
(
$
query_id
===
123
)
{
$
query_args
[
'
order
'
]
=
'
DESC
'
;
}
// Always return the $query_args.
return
$
query_args
;
}
The query class: Search_Filter\Queries\Query
The query instance class.
Function: get_attributes()
Description: Gets all the attributes for a query (most of the settings you can see in the query editor).
Return: associative array of attributes.
Use:
$query->get_attributes()
Function: get_attribute( $attribute_name )
Description: Gets a single attribute by name.
Return: attribute value or
null
if attribute not found.
Use:
$query->get_attribute('singleIntegration')
Function: get_id()
Description: Gets the query ID.
Return: the ID.
Use:
$query->get_id()
Find a query
Returns:
Search_Filter\Queries\Query or a WP_Error if not found.
By name
$
query
=
\
Search_Filter
\
Queries
\
Query
::
find
(
array
(
'
name
'
=>
'
My query
'
,
// My query
)
)
;
var_dump
(
$
query
)
;
By ID
$
query
=
\
Search_Filter
\
Queries
\
Query
::
find
(
array
(
'
id
'
=>
123
,
)
)
;
var_dump
(
$
query
)
;
Find multiple queries
Returns:
array of Search_Filter\Queries\Query
Find queries by status
$
queries
=
\
Search_Filter
\
Queries
::
find
(
array
(
'
status
'
=>
'
enabled
'
,
// Only get enabled queries.
'
number
'
=>
0
,
// Get all.
)
)
;
var_dump
(
$
queries
)
;
Find queries by integration type
$
queries
=
\
Search_Filter
\
Queries
::
find
(
array
(
'
status
'
=>
'
enabled
'
,
// Only get enabled queries.
'
number
'
=>
0
,
// Get all.
'
meta_query
'
=>
array
(
array
(
'
key
'
=>
'
integration_type
'
,
'
value
'
=>
'
single
'
,
'
compare
'
=>
'
=
'
,
),
),
)
)
;
var_dump
(
$
queries
)
;
Check if filtering has been applied
// Get the query by ID.
$
query
=
\
Search_Filter
\
Queries
\
Query
::
find
(
array
(
'
id
'
=>
123
,
// Replace 123 with your query ID.
)
)
;
$
has_filtering
=
false;
// Get the fields that belong to the query.
$
fields
=
$
query
->
get_fields
()
;
// Loop through all the fields of the query
foreach
(
$
fields
as
$
field
)
{
// Check to see if a value has been set.
if
(
!
empty
(
$
field
->
get_values
()
)
)
{
$
has_filtering
=
true;
break;
}
}
var_dump
(
$
has_filtering
)
;
JavaScript
Get an array of all queries on the page.
const
queries
=
window
.
searchAndFilter
.
frontend
.
queries
.
getAll
()
;
for
(
let
i
=
0
;
i
<
queries
.
length
;
i
++
)
{
const
query
=
queries
[
i
]
;
// Get the query ID.
console
.
log
(
query
.
getId
() )
;
// Get query attributes using getAttribute
console
.
log
(
query
.
getAttribute
(
'
postTypes
'
) )
;
console
.
log
(
query
.
getAttribute
(
'
resultsDynamicUpdate
'
) )
;
}
Get a single query by ID.
const
queryId
=
123
;
// Replace `123` with your query ID.
const
query
=
window
.
searchAndFilter
.
frontend
.
queries
.
get
(
queryId
)
;
if
(
query
)
{
// Get the query ID.
console
.
log
(
query
.
getId
() )
;
// Get query attributes using getAttribute
console
.
log
(
query
.
getAttribute
(
'
postTypes
'
) )
;
console
.
log
(
query
.
getAttribute
(
'
resultsDynamicUpdate
'
) )
;
}
Detect start/finish of fetching results
const
queryId
=
123
;
// Replace `123` with your query ID.
const
query
=
window
.
searchAndFilter
.
frontend
.
queries
.
get
(
queryId
)
;
if
(
query
)
{
// Only hook in to the update if dynamic update is enabled for the query.
if
(
query
.
getAttribute
(
'
resultsDynamicUpdate
'
)
===
'
yes
'
)
{
// Listen for the update to the results.
query
.
on
(
'
get-results/start
'
,
function
(
queryObject
)
{
console
.
log
(
"
Start getting results.
"
)
;
}
)
;
// Listen for the update to the results.
query
.
on
(
'
get-results/finish
'
,
function
(
queryObject
)
{
console
.
log
(
"
Finished getting results.
"
)
;
}
)
;
}
}
On This Page
PHP
Filter query args
The query class: Search_Filter\Queries\Query
Find a query
Find multiple queries
Find queries by integration type
Check if filtering has been applied
JavaScript
Get an array of all queries on the page.
Get a single query by ID.
Detect start/finish of fetching results
More From This Series
Developer
Queries
Fields
Theme Integration
Custom query integration
Changelogs

---

## Queries Overview - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/queries/queries-overview/

Queries are the backbone of your site. From search, to blogs, to products listings and more, they power your website in many different ways.
With Search & Filter, you can select the different queries across your site, choose to modify them, and attach fields such as search and filters to them (optional).
The most important first step is to choose which query you want to integrate with.
Integrate with a query
The first step is to create a query integration.
Head to the
Queries
tab in the
Search & Filter dashboard
.
Then
Add New
.
You’ll be presented with query integration options.
Single Post/Page/CPT
These include queries that are embedded in a single post. We support:
Query Block
WooCommerce Products Query block
Custom (Pro)
Shortcodes (Pro)
Archive
Archives can include your:
Blog
listing
Tags and categories
Custom post types
Custom taxonomies
More information about archive queries.
Search (default)
Every WordPress website comes with a search results list – it is located at a URL like:
yoursite.com/?s=
The addition of the
?s
in the URL that triggers the search behaviour of your site.
WooCommerce Shop
If you have WooCommerce enabled, you’ll see the option to integrate with your WooCommerce shop.
The shop page usually resides at a URL like:
yoursite.com/shop/
This can be changed in the WooCommerce configuration.
On This Page
Integrate with a query
Single Post/Page/CPT
Archive
Search (default)
WooCommerce Shop
More From This Series
Queries
Queries Overview
Query Editor
Live Search (Pro)
Results Shortcode (Pro)
Archives

---

## GenerateBlocks - Search & Filter Pro
**Source:** https://searchandfilter.com/documentation/integrations/generateblocks/

The
Search & Filter – GenerateBlocks Extension
allows for seamless integration between GenerateBlocks 2 and Search & Filter.
With this extension, Search & Filter will now be able to directly integrate and filter the
GenerateBlocks Query block
.
This includes support for
Full Site Editing
and archive locations.
Install + activate the extension
To get started first we need to enable the integration in our integrations screen.
Ensure you have
GenerateBlocks
enabled.
Then from the Integrations screen, click
install extension
.
The extension plugin will be automatically downloaded in the background and then enabled.
If there are any issues downloading the extension, you can
download it from your account
and install it manually.
Add the GenerateBlocks Query
Add a new GenerateBlocks Query block to your page and choose a layout to start with.
Once added, from the inspector sidebar ensure you set the following options:
Set
Query Type
to
Search & Filter Query
Select your query from the
Choose a Query
dropdown.
Create a Search & Filter query
From here you can choose to
Add New
(if you don’t have any queries yet) or
Edit
and existing Search & Filter query.
In your query, ensure that location is set to
dynamic
and then choose
GenerateBlocks
from the dropdown:
Give your query a
name
, hit
save
and your query is good to go (we’d also recommend to also enable
Live Search
while you’re here).
There are a lot of settings
to fine tune your results.
Now that you’ve connected the GenerateBlocks
Query block
with a
Search & Filter Query
we’re ready to add some fields.
Create a field
Search & Filter provides multiple blocks for adding fields:
Search
Choice
Range
Advanced
Control
You can
read more about the different types of fields here
.
Lets start by adding a
Search field block
.
When creating fields for queries, ensure the
query integration
option is set to the correct query you created earlier.
Read more about fields here
.
Lets also ensure auto submit is enabled:
Once you’re done, hit
Publish
and you should be good to go! Your page might look something like this:
Full Site Editing & Archives
Setting up archives with Full Site Editing requires a slightly different setup.
Search & Filter Query
Ensure the your query is setup to use:
Location
->
Archive
Post Type
->
Post
(choose the post type archive you want to filter)
GenerateBlocks Query Block
To use an archive ensure:
Query Type
is set to
Post Query
Inherit query from template
is enabled
On This Page
Install + activate the extension
Add the GenerateBlocks Query
Create a Search & Filter query
Create a field
Full Site Editing & Archives
Search & Filter Query
GenerateBlocks Query Block
More From This Series
Integrations
Elementor
Beaver Builder
Relevanssi
GenerateBlocks
WPML
Polylang
Dynamic Content for Elementor
Easy Digital Downloads
Divi
WPBakery Page Builder

---

