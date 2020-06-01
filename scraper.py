import re

from bs4 import BeautifulSoup

from ui_flow_navigation import order_pool_executor

HTML = """<html><head>
    <meta charset="utf-8">
    <title>IBM Store</title>
    <base href="/">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link id="appFavicon" rel="icon" type="image/x-icon" href="favicon.ico">
  <link rel="stylesheet" href="styles.3225fd679c46542ca07d.css"><style>[_nghost-c0]{display:block}.favicon[_ngcontent-c0]{display:none}</style><style>.bx--top-nav[_ngcontent-c1]{height:52px;background-color:#0f212e;z-index:6001;padding-left:0}.bx--top-nav[hidden][_ngcontent-c1]{display:none}.bx--top-nav[_ngcontent-c1]   .bx--global-header__left-container[_ngcontent-c1]   .brand-wrapper[_ngcontent-c1]{text-decoration:none;display:flex;height:100%}.bx--top-nav[_ngcontent-c1]   .bx--global-header__left-container[_ngcontent-c1]   .brand-wrapper[_ngcontent-c1]   .logo-wrapper[_ngcontent-c1]{display:flex}.bx--top-nav[_ngcontent-c1]   .bx--global-header__left-container[_ngcontent-c1]   .brand-wrapper[_ngcontent-c1]   .logo-wrapper[_ngcontent-c1]   img.logo[_ngcontent-c1]{display:block;margin:auto 24px;max-width:380px;height:26px}.bx--top-nav[_ngcontent-c1]   .bx--global-header__left-container[_ngcontent-c1]   .brand-wrapper[_ngcontent-c1]   .logo-wrapper[_ngcontent-c1]   img.logo.default-logo[_ngcontent-c1]{height:20px}.bx--top-nav[_ngcontent-c1]   .bx--global-header__left-container[_ngcontent-c1]   .brand-wrapper[_ngcontent-c1]   .header-title[_ngcontent-c1]{display:flex;align-items:center;margin-left:16px;margin-right:32px;max-width:250px}.bx--top-nav[_ngcontent-c1]   .bx--global-header__left-container[_ngcontent-c1]   .brand-wrapper[_ngcontent-c1]   .header-title[_ngcontent-c1]   h1.bx--logo__text[_ngcontent-c1]{margin:0;line-height:30px}.bx--top-nav[_ngcontent-c1]   .bx--global-header__left-container[_ngcontent-c1]   .brand-wrapper[_ngcontent-c1]   .header-title[_ngcontent-c1]   .bx--logo__text[_ngcontent-c1]{font-weight:300;font-family:ibm-plex-sans,IBMHelvetica,Helvetica Neue,Helvetica,Arial,sans-serif;font-size:1rem;color:#fff;display:inline-block}.bx--top-nav[_ngcontent-c1]   .bx--global-header__left-container[_ngcontent-c1]   .bx--global-header__menu[_ngcontent-c1]{color:#dfe9e9;background:0 0;width:inherit}.bx--top-nav[_ngcontent-c1]   .bx--global-header__left-container[_ngcontent-c1]   .bx--global-header__menu[_ngcontent-c1] > li[_ngcontent-c1] > a[_ngcontent-c1]{padding-top:5px;background:0 0;color:#5596e6;font-size:.875rem!important;font-weight:600!important;white-space:nowrap}.bx--top-nav[_ngcontent-c1]   .bx--global-header__left-container[_ngcontent-c1]   .bx--global-header__menu[_ngcontent-c1] > li[_ngcontent-c1] > a.active[_ngcontent-c1]{padding-top:10px;color:#fff;border-bottom:5px solid #fff}.bx--top-nav[_ngcontent-c1]   .bx--global-header__left-container[_ngcontent-c1]   .bx--global-header__menu[_ngcontent-c1] > li[_ngcontent-c1] > a[_ngcontent-c1]:hover{color:#fff}.bx--top-nav[_ngcontent-c1]   .bx--global-header__right-container[_ngcontent-c1]{background-color:transparent!important;padding:0}h1.bx--logo__text[_ngcontent-c1]{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-family:IBMHelvetica,Helvetica Neue,Helvetica,Arial,sans-serif}#orders-overflow-menu-container.bx--overflow-menu--flip[_ngcontent-c1]{left:0;border:1px solid #276fae}#orders-overflow-menu-container.bx--overflow-menu--flip[_ngcontent-c1]:before{left:40px}ul#orders-overflow-menu-container[_ngcontent-c1] > li[_ngcontent-c1] > a.bx--overflow-menu-options__btn[_ngcontent-c1]{border:1px solid #fff;text-decoration:none;color:#000;height:40px}a#ordersLinkId[_ngcontent-c1]{padding-top:5px;background:0 0;color:#5596e6;font-size:.875rem!important;font-weight:600!important;white-space:nowrap}a#ordersLinkId.active[_ngcontent-c1]{padding-top:10px;color:#fff;border-bottom:5px solid #fff}a#approverOrdersLinkId[_ngcontent-c1]:hover, a#myordersLinkId[_ngcontent-c1]:hover{color:#fff!important;background-color:transparent!important}</style><style>header[_ngcontent-c2]{height:125px;color:#fff;display:block;position:fixed}header[_ngcontent-c2]   .left[_ngcontent-c2]{float:left;width:50%}header[_ngcontent-c2]   .right[_ngcontent-c2]{float:right;width:50%}.bx--global-header[_ngcontent-c2]{box-shadow:0 6px 12px 0 rgba(0,0,0,.1);width:100%;position:fixed;top:52px;left:0;display:flex;justify-content:space-between;line-height:1.95;z-index:9000;height:7.5rem;color:#fff}</style><style>.bx--loading--static[_ngcontent-c3] {
        position: static;
      }

      .bx--loading--medium[_ngcontent-c3] {
        width: 4rem;
        height: 4rem;
      }

      .bx--loading-overlay[_ngcontent-c3] {
        z-index: 99;
      }</style><style></style><style>#api-key-modal-id[_ngcontent-c8]     .bx--modal-content{overflow:unset}</style><style>.remove[_ngcontent-c10]{
        border-top: #E42238 4px solid;
      }</style><style>.bx--toolbar__menu__icon[_ngcontent-c12] {
          width: 100%;
          height: 100%;
          fill: #5a6872
        }

        .bx--overflow-menu__icon[_ngcontent-c12] {
          display: block;
        }</style><style>header[_ngcontent-c9]{height:125px;color:#fff;display:block;position:fixed}header[_ngcontent-c9]   .left[_ngcontent-c9]{float:left;width:50%}.bx--global-header[_ngcontent-c9]{box-shadow:0 6px 12px 0 rgba(0,0,0,.1);width:100%;position:fixed;top:52px;left:0;display:flex;justify-content:space-between;line-height:1.95;z-index:9000;height:105px;color:#fff}.bx--global-header.suite-mode[_ngcontent-c9]{top:0}</style><script charset="utf-8" src="169.73d2536d017b6cdefdad.js"></script><style>[_nghost-c13]{display:block;background-color:#1d3548}[_nghost-c13]   .full-page[_ngcontent-c13]{min-height:100vh;display:flex;flex-direction:column}[_nghost-c13]   .full-page[_ngcontent-c13]   footer[_ngcontent-c13]{margin-top:auto;display:inline-block;width:100%}[_nghost-c13]   .home[_ngcontent-c13]{padding-bottom:100px}[_nghost-c13]   .home[_ngcontent-c13]   .links[_ngcontent-c13]{margin-top:40px}[_nghost-c13]   .home[_ngcontent-c13]   img.logo[_ngcontent-c13]{max-width:90%;max-height:220px;margin-top:40%;margin-left:auto;margin-right:auto;display:block}[_nghost-c13]   .home[_ngcontent-c13]   .welcome[_ngcontent-c13]{padding-top:37%;color:#fff;font-size:larger}[_nghost-c13]   .home[_ngcontent-c13]   .title[_ngcontent-c13]{color:#fff;font-size:2.5rem;padding-top:20px;font-weight:600}[_nghost-c13]   .home[_ngcontent-c13]   .details[_ngcontent-c13]{color:#fff;margin-top:10px;font-size:.875rem;line-height:1.25rem;font-weight:200;padding-top:20px;overflow-y:auto;max-height:15rem}a#privacy-policy[_ngcontent-c13]{background-color:transparent;color:#3d70b2}a#privacy-policy[_ngcontent-c13]:hover{background-color:#3d70b2;color:#fff}#copyright-footer[_ngcontent-c13]{float:right;color:#fff;padding:0 10px 20px 0}#privacy-statement[_ngcontent-c13]     .bx--modal-container{min-width:650px}#privacy-statement[_ngcontent-c13]     .bx--modal-content{overflow:visible}#privacy-policy-link[_ngcontent-c13]{cursor:pointer}carbon-modal[_ngcontent-c13]   p[_ngcontent-c13]{margin-bottom:10px}carbon-modal[_ngcontent-c13]   ul[_ngcontent-c13]{list-style:disc;padding-left:40px}carbon-modal[_ngcontent-c13]   carbon-notification[_ngcontent-c13]   .body[_ngcontent-c13], carbon-modal[_ngcontent-c13]   carbon-notification[_ngcontent-c13]   .title[_ngcontent-c13]{font-size:.75rem}</style><script charset="utf-8" src="3.162d385821dfc0e67ecb.js"></script><script charset="utf-8" src="common.1a5b3e6058acda44c732.js"></script><script charset="utf-8" src="163.84d28d6e200a4b6ca34b.js"></script><script charset="utf-8" src="4.eca0fbef888c2dbfb34d.js"></script><script charset="utf-8" src="165.3dae3d25f44b7d15939e.js"></script><script charset="utf-8" src="167.254db80b1eab9b48773b.js"></script><script charset="utf-8" src="168.633df10181bd943e6d55.js"></script><script charset="utf-8" src="1.65518a076b2cb7656f03.js"></script><script charset="utf-8" src="162.8fe491d7a6dcea22c9f5.js"></script><script charset="utf-8" src="164.53f23b71025d3cb7c272.js"></script><script charset="utf-8" src="171.2904279e5aa1848adf08.js"></script><script charset="utf-8" src="161.c0e3f1cd6eaf30e18b0d.js"></script><script charset="utf-8" src="160.44bef907643b9dfd0838.js"></script><script charset="utf-8" src="170.0088c60f8dd9bd37a6b4.js"></script><script charset="utf-8" src="166.bf2c55021e275c9a635e.js"></script><style>.bx--cloud-header-list__btn[_ngcontent-c6]{font-family:ibm-plex-sans,Helvetica Neue,Arial,sans-serif;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;letter-spacing:.5px;background:0 0;-webkit-appearance:none;-moz-appearance:none;border:0;cursor:pointer;display:flex;align-items:center;padding:0 7px}.help-icon[_ngcontent-c6]{width:20px;height:20px}</style><style>.bx--overflow-menu[_ngcontent-c7]{height:0}.bx--overflow-menu-options[_ngcontent-c7]{z-index:2;margin-top:10px}.bx--overflow-menu-options__btn[_ngcontent-c7]{word-wrap:break-word}.bx--overflow-menu--flip[_ngcontent-c7]{left:-150px}.bx--overflow-menu--flip[_ngcontent-c7]:before{left:162px}.bx--cloud-header-list__btn[_ngcontent-c7]{font-family:ibm-plex-sans,Helvetica Neue,Arial,sans-serif;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;letter-spacing:.5px;color:#fff;background:0 0;-webkit-appearance:none;-moz-appearance:none;border:0;cursor:pointer;display:flex;align-items:center;padding:0 7px}.bx--cloud-header-list__btn[_ngcontent-c7]   .user-icon[_ngcontent-c7]{width:20px;height:20px}.bx--cloud-header-list__btn[_ngcontent-c7]   span[_ngcontent-c7]{padding-left:5px;margin:auto}.bx--cloud-header-list__btn[_ngcontent-c7]   span[_ngcontent-c7] > svg[_ngcontent-c7]{color:#fff;fill:currentColor}#profile[_ngcontent-c7]{display:flex}</style><style>#selected-cart[_ngcontent-c5]{display:flex}#selected-cart[_ngcontent-c5]   span.selected-cart-name[_ngcontent-c5]{display:inline-block;margin:auto 0;max-width:200px;color:#fff}#selected-cart[_ngcontent-c5]   span.count[_ngcontent-c5]{display:inline-block;line-height:25px;text-align:center;color:#5596e6;background:#fff;min-width:23px;height:23px;border-radius:50%;margin-left:5px;font-size:.875rem}#selected-cart[_ngcontent-c5]   .bx--cloud-header-list__btn[_ngcontent-c5]{font-family:ibm-plex-sans,Helvetica Neue,Arial,sans-serif;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;letter-spacing:.5px;color:#fff;background:0 0;-webkit-appearance:none;-moz-appearance:none;border:0;cursor:pointer;display:flex;align-items:center;padding:0 7px}#selected-cart[_ngcontent-c5]   .bx--cloud-header-list__btn[_ngcontent-c5]   .cart-icon[_ngcontent-c5]{width:20px;height:20px}#selected-cart[_ngcontent-c5]   .bx--cloud-header-list__btn[_ngcontent-c5]   span[_ngcontent-c5]{padding-left:5px;margin:auto}#selected-cart[_ngcontent-c5]   .bx--cloud-header-list__btn[_ngcontent-c5]   span[_ngcontent-c5] > svg[_ngcontent-c5]{color:#fff;fill:currentColor}.bx--overflow-menu[_ngcontent-c5]{height:0}.bx--overflow-menu--flip[_ngcontent-c5]{left:-132px}.bx--overflow-menu-options[_ngcontent-c5]{z-index:2;margin-top:10px}.bx--overflow-menu-options__btn[_ngcontent-c5]{max-width:11.25rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.scroll-class[_ngcontent-c5]{max-height:550px;overflow:auto;width:100%}.toolbar-menu__title[_ngcontent-c5]{font-size:.875rem;font-weight:600;padding:.5rem 1rem}button[_ngcontent-c5]:focus{outline:0}span.selected-cart-name[_ngcontent-c5]{font-size:.875rem;white-space:nowrap;overflow-y:visible;overflow-x:hidden;text-overflow:ellipsis;padding:1px 0;line-height:1.2em}</style><style>.main-services-container[_ngcontent-c15]{display:flex;min-height:100vh;background-color:#f5f7fa}.services-wrapper[_ngcontent-c15]{display:flex;flex-direction:column;flex-basis:100%;height:100%;margin-left:270px}.services-wrapper[_ngcontent-c15]   .notification[_ngcontent-c15]{margin:1.5rem auto;width:25%}.header-category[_ngcontent-c15]{font-weight:700;font-size:20px;color:#20343e;padding-bottom:5px;margin-left:2rem;margin-top:3.5rem;display:block;clear:both}.header-subcategory[_ngcontent-c15]{font-size:24px;color:#5a6872;margin-left:2rem;margin-top:2rem;display:block}.services-box[_ngcontent-c15]{margin-top:30px}.floating-box[_ngcontent-c15]{float:left;margin:20px}.service-tabs[_ngcontent-c15]{padding-left:250px;background-color:#264a60;position:fixed;top:150px;width:100%;z-index:1;height:40px;display:flex;justify-content:flex-end}.service-tabs[_ngcontent-c15]   .search[_ngcontent-c15]{width:430px;margin-right:-2rem}.service-tabs.suite-mode[_ngcontent-c15]{top:105px}.content[_ngcontent-c15]{margin-top:157px}.content.suite-mode[_ngcontent-c15]{margin-top:105px}store-filter-menu[_ngcontent-c15]     .wrapper{width:272px;background-color:#dfe6eb}.tooltip-text-wrapper[_ngcontent-c15]{word-wrap:break-word;z-index:1000;position:absolute}carbon-search[_ngcontent-c15]     .bx--search-input{cursor:pointer;font-size:.75rem;padding-left:2.25rem;padding-right:1rem}carbon-search[_ngcontent-c15]     input::-webkit-input-placeholder{color:#fff}carbon-search[_ngcontent-c15]     input:-ms-input-placeholder{color:#fff}carbon-search[_ngcontent-c15]     input::-ms-input-placeholder{color:#fff}carbon-search[_ngcontent-c15]     input::placeholder{color:#fff}carbon-search[_ngcontent-c15]     .bx--search-magnifier{fill:#fff}carbon-search[_ngcontent-c15]     .bx--search{width:80%}</style><style>[_nghost-c16]{position:relative;z-index:0}.is-active[_nghost-c16]{z-index:1}.bx--dropdown-wrapper   [_nghost-c16]   .bx--search__trigger[_ngcontent-c16]{padding:10px;background:#fff;border-bottom:1px solid #dfe3e6;position:relative}.bx--dropdown-wrapper   [_nghost-c16]   .bx--search__trigger[_ngcontent-c16]   .bx--search-close[_ngcontent-c16], .bx--dropdown-wrapper   [_nghost-c16]   .bx--search__trigger[_ngcontent-c16]   .bx--search-magnifier[_ngcontent-c16]{right:1.25rem}.bx--search[_ngcontent-c16]{height:100%;position:relative}.bx--search.is-disabled[_ngcontent-c16]{opacity:.5;cursor:not-allowed}.bx--search.is-disabled[_ngcontent-c16]:before{content:'';width:100%;height:100%;position:absolute;top:0;left:0;z-index:1}.bx--search.is-actionable[_ngcontent-c16]   .bx--search-input[_ngcontent-c16]{padding-left:1em;width:100%}.bx--search.is-actionable[_ngcontent-c16]   .bx--search-close[_ngcontent-c16], .bx--search.is-actionable[_ngcontent-c16]   .bx--search-magnifier[_ngcontent-c16]{left:inherit;right:.75rem}input[type=text][_ngcontent-c16]:focus{border:1px solid #3d70b2;transition:.2s}.bx--search__wrapper[_ngcontent-c16]{display:flex;position:relative;flex-grow:1;flex-direction:column;width:100%}.bx--search-close[_ngcontent-c16]{transition:.2s}.bx--search--white[_ngcontent-c16]   .bx--search-input[_ngcontent-c16]{color:#fff}.bx--search--white[_ngcontent-c16]   .bx--search-close[_ngcontent-c16], .bx--search--white[_ngcontent-c16]   .bx--search-magnifier[_ngcontent-c16]{fill:#fff}.bx--search--white[_ngcontent-c16]   [_ngcontent-c16]::-webkit-input-placeholder{color:#fff}.bx--search--white[_ngcontent-c16]   [_ngcontent-c16]::-moz-placeholder{color:#fff}.bx--search--white[_ngcontent-c16]   [_ngcontent-c16]:-ms-input-placeholder{color:#fff}.bx--search-close--hidden[_ngcontent-c16]{display:none}.bx--form-requirement[_ngcontent-c16]{max-height:inherit}.bx--form-requirement.is-invalid[_ngcontent-c16]{max-height:12.5rem;display:block}.bx--search-magnifier[_ngcontent-c16]:focus, .bx--search-magnifier[_ngcontent-c16]:hover{fill:#3d70b2;cursor:pointer;z-index:1}.bx--search-magnifier.bx--search-magnifier--hidden[_ngcontent-c16]{display:none}.bx--search-dropdown[_ngcontent-c16]{position:absolute;top:100%;left:0;width:100%;z-index:1;background:#fff;box-shadow:0 2px 5px -2px rgba(0,0,0,.25);overflow:auto;max-height:12em}.bx--search-dropdown.bx--search-dropdown--inline[_ngcontent-c16]{position:relative;top:0}.bx--search-dropdown[_ngcontent-c16]   li[_ngcontent-c16]{width:100%}.bx--search-dropdown--option[_ngcontent-c16]{padding:10px 16px;font-size:14px;line-height:1em;cursor:pointer;text-overflow:ellipsis;overflow:hidden}.bx--search-dropdown--option.selected[_ngcontent-c16], .bx--search-dropdown--option[_ngcontent-c16]:focus, .bx--search-dropdown--option[_ngcontent-c16]:hover{background:#3d70b2;color:#fff}.bx--search-dropdown--option[_ngcontent-c16]:last-child{margin-bottom:8px}.bx--search-dropdown--option.is-bordered[_ngcontent-c16]{border-bottom:1px solid #dfe3e6}.bx--search-dropdown--more[_ngcontent-c16]{color:#3d70b2;font-weight:700}.bx--search-dropdown--empty[_ngcontent-c16]{font-size:14px;line-height:1.3em;padding:24px 0;text-align:center}</style><style>.wrapper[_ngcontent-c17]{width:240px;background-color:#dfe6eb;float:left;overflow-y:scroll;position:fixed;z-index:1000;white-space:nowrap;padding:20px;top:10rem;bottom:0;box-shadow:0 1px 4px 0 #6d7777}.wrapper.suite-mode[_ngcontent-c17]{top:145px}.wrapper[_ngcontent-c17]::-webkit-scrollbar-track{-webkit-box-shadow:inset 0 0 6px #dfe6eb;border-radius:10px;background-color:#dfe6eb}.wrapper[_ngcontent-c17]::-webkit-scrollbar{width:6px;background-color:#dfe6eb}.wrapper[_ngcontent-c17]::-webkit-scrollbar-thumb{border-radius:10px;-webkit-box-shadow:inset 0 0 6px #fff;background-color:#5a6872}div.main[_ngcontent-c17]{clear:both;padding-top:25px;padding-bottom:15px}div.main-provider[_ngcontent-c17]{clear:both;padding-top:20px}.filter[_ngcontent-c17]   .reset[_ngcontent-c17]{float:right;padding-right:10px;font-size:x-small;line-height:16px}.filter[_ngcontent-c17]   .filter-by[_ngcontent-c17]{float:left;font-weight:700;font-size:18px;color:#20343e}.filter[_ngcontent-c17]   .reset[_ngcontent-c17]   a[_ngcontent-c17]{cursor:pointer}.selected-terms[_ngcontent-c17]{font-size:12px;font-style:italic;padding-left:5px;padding-top:5px;color:grey;clear:both}.bx--checkbox-label[_ngcontent-c17]{color:#9da0a2}.provider_label[_ngcontent-c17]{text-transform:capitalize;font-weight:700;padding-left:1.25rem;font-size:1.125rem;color:#20343e}.category_label[_ngcontent-c17]{float:left;font-weight:700;font-size:18px;color:#20343e}img.filter-img[_ngcontent-c17]{float:left;height:1.25rem;padding-top:.25rem;padding-right:1rem;vertical-align:middle}img.category-img[_ngcontent-c17]{float:left;padding-right:1rem;vertical-align:middle}div.provider-internal-container[_ngcontent-c17]{display:block;flex-direction:column;justify-content:space-evenly;background-color:#f5f7fa;overflow-y:auto;white-space:initial;height:15rem;padding:3px}div.category-internal-container[_ngcontent-c17]{display:block;flex-direction:column;justify-content:space-evenly;min-height:20rem;background-color:#f5f7fa;overflow-y:auto;white-space:initial;max-height:20rem;padding:3px}.filter-left-nav[_ngcontent-c17]{font-size:.875rem}</style><style>button[_ngcontent-c11]  {
        padding: 0;
      }

      .bx--inline-notification[_nghost-c11] {
        display: none;
      }

      .bx--inline-notification.bx--toast-notification-show[_nghost-c11] {
        display: flex;
      }

      .bx--toast-notification[_nghost-c11] {
        position: fixed;
        top: 0.5rem;
        right: 0px;
        display: flex;
        flex-direction: row;
        width: 23rem;
        opacity: 0;
        margin-top: 0.5rem;
        z-index: 6001;
        transform: translate3d(calc(100% + 1rem), 0, 0);
        transition: opacity 0s cubic-bezier(1, 0, 1, 0) 0.3s, transform 0s cubic-bezier(1, 0, 1, 0) 0.5s;
      }

      .bx--toast-notification-show[_nghost-c11] {
        opacity: 1;
        z-index: 6002;
        transform: translate3d(0%, 0, 0);
        transition: transform 0.5s ease-in;
      }</style><style>.first-level[_ngcontent-c20]{padding-left:10px;margin:3px}.forth-level[_ngcontent-c20], .second-level[_ngcontent-c20], .third-level[_ngcontent-c20]{display:none;padding-left:1rem}.third-level[_ngcontent-c20]{padding-left:30px}.forth-level[_ngcontent-c20]{padding-left:40px}.visible[_ngcontent-c20]{display:block}.menu-item[_ngcontent-c20]{padding-top:5px;padding-bottom:5px}li[_ngcontent-c20]{color:grey;clear:both}li[_ngcontent-c20]   carbon-icon[_ngcontent-c20]{cursor:pointer}li[_ngcontent-c20]   carbon-checkbox[_ngcontent-c20]{float:left}li[_ngcontent-c20]   a[_ngcontent-c20]{color:grey}</style><style>.checkbox-disabled[_ngcontent-c14], .bx--label--disabled[_ngcontent-c14] {
        opacity: 0.5;
        pointer-events: none;
      }</style><style>carbon-card[_ngcontent-c18]     .bx--card__card-overview{font-size:14px;font-weight:300;padding-left:8px;padding-top:8px;padding-right:8px;color:#20343e;line-height:30px;border-top:5px solid #3d70b2;flex-direction:column}carbon-card[_ngcontent-c18]     .bx--card__card-overview:hover{cursor:pointer}carbon-card[_ngcontent-c18]     .bx--card-footer{background-color:#fff}carbon-card[_ngcontent-c18]     .bx--card{height:18.2rem}carbon-card[_ngcontent-c18]     .bx--card:hover{border-left:2px solid #f0f3f6;border-right:2px solid #f0f3f6;border-bottom:2px solid #f0f3f6;box-shadow:0 12px 16px 0 rgba(0,0,0,.24),0 17px 50px 0 rgba(0,0,0,.19);-webkit-transform:scale(1.03);transform:scale(1.03);transition:all .5s}tooltip-wrapper[_ngcontent-c18]     .bx--tooltip{padding:.5rem}.card-service-tooltip[_ngcontent-c18]{white-space:pre-wrap;overflow-wrap:break-word;word-break:break-all;font-size:12px}.hidden-service-ID[_ngcontent-c18]{visibility:hidden}.service-detail[_ngcontent-c18]{margin-top:.5rem;margin-left:.65rem;display:flex;flex-direction:column;align-items:flex-start;width:100%;flex-basis:10%}.service-price[_ngcontent-c18]{font-size:1rem;font-weight:500;color:#3d70b2;text-overflow:ellipsis;margin-top:.25rem}.service-box[_ngcontent-c18]{margin:1.25rem;float:left}.service-box[_ngcontent-c18]   .card-provider-name[_ngcontent-c18]{font-weight:700;font-size:15px;text-transform:uppercase;color:#20343e;text-align:left;margin-top:1rem}.service-box[_ngcontent-c18]   .card-service-name[_ngcontent-c18]{font-weight:400;font-size:12px;color:#20343e;text-align:left;min-height:2rem;text-overflow:ellipsis;text-transform:capitalize}.service-box[_ngcontent-c18]   .card-service-title[_ngcontent-c18]{font-size:1.125rem;font-weight:700;text-overflow:ellipsis;text-align:left}.service-box[_ngcontent-c18]   .card-description-text[_ngcontent-c18]{font-weight:300;font-size:14px;color:#20343e;line-height:30px}.service-box[_ngcontent-c18]   .card-small-font[_ngcontent-c18]{font-size:1rem;font-weight:500;color:#8c9ba5;margin-top:.875rem}.service-box[_ngcontent-c18]   .card-blue-large-font[_ngcontent-c18]{color:#5aaafa;font-size:.8rem;padding-top:1rem}.service-box[_ngcontent-c18]   carbon-card-overview[id^=storefront_carbon-card][_ngcontent-c18]{cursor:pointer}.service-box[_ngcontent-c18]   .bx--about__icon[_ngcontent-c18]{width:4.125rem;height:4.125rem}.service-box[_ngcontent-c18]   .bx--about__icon[_ngcontent-c18]   .bx--about__icon--img[_ngcontent-c18]{width:3.5rem;height:2rem}.service-box[_ngcontent-c18]   img.bx--about__icon--img[_ngcontent-c18]{display:flex;margin:.75rem auto;height:2.75rem}.service-box[_ngcontent-c18]   figure[_ngcontent-c18]{height:32px;margin-top:-12px}.service-box[_ngcontent-c18]   .card-figure[_ngcontent-c18]{margin:.5rem;height:4rem;background:#f0f3f6}.service-box[_ngcontent-c18]   .card-footer[_ngcontent-c18]{width:100%;display:flex;flex-direction:row;justify-content:flex-end;margin-top:.5rem}.service-box[_ngcontent-c18]   .card-container[_ngcontent-c18]{display:flex;width:100%;flex-basis:100%;flex-direction:column;align-items:stretch;border-top:5px solid #3d70b2}.service-box[_ngcontent-c18]   .card-container[_ngcontent-c18]:hover{cursor:pointer}carbon-button[_ngcontent-c18]     .bx--btn--primary{min-width:100px}carbon-button[_ngcontent-c18]     .bx--btn--secondary{min-width:100px}</style><style>[_nghost-c21] {
        position: relative;
      }

      .tooltip-wrapper[_ngcontent-c21] {
        display: inline-block;
        text-align: center;
        width: 200px;
        padding: 25px;
        background-color: #fff;
      }

      .tooltip-content[_ngcontent-c21] {
        z-index: 1000;
      }</style><style>[_nghost-c22] {
        display: block;
        position: absolute;
        width: 15rem;
      }

      .data-table-tooltip[_nghost-c22]   .bx--tooltip[_ngcontent-c22] {
        padding: .8rem 1rem;
      }

      .bx--tooltip[_ngcontent-c22] {
        word-wrap: break-word;
        padding: 0.5rem;
        z-index: 99999;
      }
      .bx--tooltip[_ngcontent-c22]   .bx--tooltip-overlow[_ngcontent-c22] {
        max-height: 6rem;
        overflow: auto;
      }
      .floating-menu-direction-top.bx--tooltip[_ngcontent-c22]:before {
          top: auto;
          bottom: -0.375rem;
          -webkit-transform: rotate(45deg);
          transform: rotate(45deg);
      }</style><style>.configure-service[_ngcontent-c23]{color:#fff;font-size:20px;font-weight:Bold}.content[_ngcontent-c23]{margin-top:80px}.content[_ngcontent-c23]   .left[_ngcontent-c23]{margin-left:50px;width:25%}.content[_ngcontent-c23]   .right[_ngcontent-c23]{width:40%;margin-right:25%}.tooltip[_ngcontent-c23]{position:absolute;right:-16px;top:0}.relative-parent[_ngcontent-c23]{position:relative}#service-name[_ngcontent-c23]   .tooltiptext[_ngcontent-c23]{width:220px;text-align:left}.mainParamsSectionHeader[_ngcontent-c23]{border-bottom:2px solid #d3d3d3;padding-bottom:.3rem;margin-right:3%;margin-bottom:1rem}</style><style>.blueprint-name-tooltip[_ngcontent-c25]{color:#000;white-space:pre-wrap;overflow-wrap:break-word;word-break:break-all}.circle-img[_ngcontent-c25]{width:120px;height:120px;border:1px solid #d3d3d3;border-radius:60px;margin-top:40px;background-color:#fff}.circle-img[_ngcontent-c25]   img[_ngcontent-c25]{width:50%;height:50%;margin:25%}.service-progress[_ngcontent-c25]{display:flex;flex-direction:row;border-bottom:2px solid #d3d3d3;height:100px;margin-top:calc(157px + 15px);justify-content:flex-start}.service-progress[_ngcontent-c25]   .left[_ngcontent-c25]{display:flex;margin-left:26px}.service-progress[_ngcontent-c25]   .left[_ngcontent-c25]   .right-progress[_ngcontent-c25]{line-height:60px;margin-left:10px;margin-top:40px;font-weight:600;font-size:1.125rem}.service-progress[_ngcontent-c25]   .left[_ngcontent-c25]   .blueprint-name[_ngcontent-c25]{display:block;overflow:hidden;padding-left:0;text-overflow:ellipsis;text-align:-webkit-left;white-space:nowrap;max-width:260px;font-size:1rem}.service-progress[_ngcontent-c25]   .progress-indicator[_ngcontent-c25]{display:flex;flex-direction:row;flex-shrink:2;max-width:1000px}</style><style>.estimated-cost[_ngcontent-c26]{font-size:14px;color:#5596e6;line-height:33px;display:block}.description[_ngcontent-c26]{text-align:left;font-size:1rem;font-weight:500;font-style:italic;line-height:25px}[_nghost-c26]   .cost[_ngcontent-c26]{margin-top:2rem}[_nghost-c26]   .cost[_ngcontent-c26]   p[_ngcontent-c26]{margin-top:1rem;color:#83d477;text-transform:capitalize}</style><style>.textbox-disabled[_ngcontent-c27] {
    opacity: 0.5;
    pointer-events: none;
  }</style><style>.required[_ngcontent-c28]{color:red}.bx--form-requirement[_ngcontent-c28]{max-height:25px;color:red;display:block}.bx--slider__track--invalid[_ngcontent-c28]{background:red}.bx--slider__range-label[_ngcontent-c28]{white-space:nowrap}.bx--slider-text-input[_ngcontent-c28], .bx-slider-text-input[_ngcontent-c28]{min-width:3.5rem;-webkit-appearance:textfield;-moz-appearance:textfield;appearance:textfield}.bx-slider-text-input[_ngcontent-c28]::-ms-clear{display:none}.bx-slider-text-input[_ngcontent-c28]::-webkit-inner-spin-button{-webkit-appearance:none;appearance:none}.bx--slider-container[_ngcontent-c28]{min-width:15.875rem}.bx--slider--disabled[_ngcontent-c28]{opacity:.5;pointer-events:none}.default-value[_ngcontent-c28]{font-size:.85em;color:gray}</style><style>.bx--dropdown-list[_ngcontent-c30]{border-radius:5px}.bx--dropdown--open[_ngcontent-c30]   .bx--dropdown-list[_ngcontent-c30]{max-height:200px;overflow:auto;outline:0}.bx--dropdown[_ngcontent-c30]:focus{outline:0;box-shadow:none;border:.75px solid #3d70b2}.bx--text-input[_ngcontent-c30]{background-color:transparent;border:.75px solid transparent}.bx--text-input[_ngcontent-c30]:focus, .bx--text-input[_ngcontent-c30]:hover{background-color:transparent;border:.75px solid transparent;box-shadow:none;outline:0}.bx--dropdown[_ngcontent-c30]{border:.75px solid transparent}.bx--dropdown[_ngcontent-c30]:hover{border:.75px solid #3d70b2}.dropdown-disabled[_ngcontent-c30]{opacity:.5;pointer-events:none}.default-value[_ngcontent-c30]{font-size:.85em;color:gray}</style><style>.required[_ngcontent-c29] {
        color: red;
      }
      .radiogroup-disabled[_ngcontent-c29] {
        opacity: 0.5;
        pointer-events: none;
      }
      .bx--radio-group--vertical[_ngcontent-c29] {
        flex-direction: column;
        align-items: flex-start;
      }</style><style>.hide[_ngcontent-c31]{display:none}.search-control[_ngcontent-c31]{margin-right:1rem;margin-bottom:.8rem}</style><style>.bx--radio-button__appearance[_ngcontent-c34]:hover {
        border-color: #3d70b2;
      }</style><style>.bx--progress-step[_ngcontent-c32]:first-child   .bx--progress-line[_ngcontent-c32]{display:inherit!important}.cursor-class[_ngcontent-c32]{cursor:pointer}.cursor-class[_ngcontent-c32]:hover{-webkit-transform:scale(1.3);transform:scale(1.3);transition:.5s}.bx--progress-label[_ngcontent-c32]{font-size:.9rem;line-height:1.3rem;word-break:break-word}.bx--progress-line[_ngcontent-c32]{opacity:.75;height:5px}.check[_ngcontent-c32]{stroke:#3d70b2;stroke-dasharray:150;stroke-dashoffset:150;-webkit-animation:2s linear forwards check;animation:2s linear forwards check}@-webkit-keyframes check{0%{stroke-dashoffset:150}50%{stroke-dashoffset:100}75%{stroke-dashoffset:75}100%{stroke-dashoffset:0}}@keyframes check{0%{stroke-dashoffset:150}50%{stroke-dashoffset:100}75%{stroke-dashoffset:75}100%{stroke-dashoffset:0}}@-webkit-keyframes circle{0%,100%{-webkit-transform:none;transform:none}50%{-webkit-transform:scale(1.1);transform:scale(1.1)}}@keyframes circle{0%,100%{-webkit-transform:none;transform:none}50%{-webkit-transform:scale(1.1);transform:scale(1.1)}}</style><style>.bx--dropdown-link[_ngcontent-c33] {
        padding-top: 13px;
        padding-bottom: 13px;
      }
      .bx--dropdown-item-disabled[_ngcontent-c33] {
        pointer-events: none;
        opacity: .5;
      }</style><style>.bx--dropdown[_ngcontent-c35]{border-radius:0;position:relative}.bx--dropdown.is-disabled[_ngcontent-c35]{opacity:.5;cursor:not-allowed}.bx--dropdown.is-disabled[_ngcontent-c35]:before{content:'';width:100%;height:100%;position:absolute;top:0;left:0;z-index:1}.bx--dropdown.is-disabled[_ngcontent-c35]:hover{box-shadow:none;border-color:transparent}.bx--dropdown-text[_ngcontent-c35]{text-overflow:ellipsis;overflow:hidden}.bx--dropdown-text.is-invalid[_ngcontent-c35]{box-shadow:0 2px 0 0 #e71d32}.bx--form-requirement.is-invalid[_ngcontent-c35]{max-height:12.5rem;display:block}.bx--dropdown-content[_ngcontent-c35]{position:absolute;width:100%;top:100%;left:0;z-index:1;height:0;overflow:hidden;display:none}.bx--dropdown-content.bx--dropdown-content--open[_ngcontent-c35]{height:auto;display:block;box-shadow:0 2px 5px -2px rgba(0,0,0,.25)}</style><style>carbon-button#additional-params-order-cancel-modal_carbon-button_no[_ngcontent-c36]{float:left;min-width:60px}.cancel[_ngcontent-c36]{padding-right:80px;cursor:pointer;text-decoration:underline}.configure-service[_ngcontent-c36]{color:#fff;font-size:20px;font-weight:Bold}.content[_ngcontent-c36]{margin-top:80px}.content[_ngcontent-c36]   .left[_ngcontent-c36]{margin-left:50px;width:25%}.content[_ngcontent-c36]   .left[_ngcontent-c36]   .left-container[_ngcontent-c36]{display:flex;flex-direction:column}.content[_ngcontent-c36]   .left[_ngcontent-c36]   .left-container[_ngcontent-c36]   .description-section[_ngcontent-c36]{max-height:80%}.content[_ngcontent-c36]   .left[_ngcontent-c36]   .left-container[_ngcontent-c36]   .price-section[_ngcontent-c36]{margin-top:20px;height:40px;max-height:20%}.content[_ngcontent-c36]   .right[_ngcontent-c36]{width:37%;margin-right:25%}.estimatedCost[_ngcontent-c36]{font-size:14px;color:#5596e6;line-height:33px;display:block;cursor:pointer}.price-update-error[_ngcontent-c36]{color:red}.price-update-loading-icon[_ngcontent-c36]{display:block;height:40px;width:100%}  li.bx--dropdown-text{white-space:nowrap}#additional-params_dynamic-form[_ngcontent-c36]     .form-field   .form-field-item{max-width:calc(100% - 16px)}#additional-params_dynamic-form[_ngcontent-c36]     .old-selection{position:absolute}</style><style>[_nghost-c37]     .dynamic-field{margin-bottom:15px}[_nghost-c37]     .dynamic-field label{display:block;font-size:16px;font-weight:400;letter-spacing:0;margin-bottom:10px;color:rgba(0,0,0,.9)}.dynamic-form[_ngcontent-c37]{max-width:60%}</style><style>.form-field[_ngcontent-c38]{position:relative;margin-bottom:20px}.no-margin[_ngcontent-c38]{margin-bottom:0}.old-selection[_ngcontent-c38]{font-size:.9em;position:absolute;left:0;bottom:0}.old-selection[_ngcontent-c38] > span[_ngcontent-c38]{font-weight:700}.error-style[_ngcontent-c38]{color:red;display:inherit;width:59.625em;font-size:.75rem;font-weight:600}</style><style>.progress-bar--select[_ngcontent-c38]{display:flex;flex-direction:column;align-items:center}carbon-dropdown[_ngcontent-c38]     .bx--form-requirement{max-height:12.5rem;color:red;display:block}</style></head>
  <body class="bx--global-light-ui">
    <div class="container">
      <app-root _nghost-c0="" ng-version="5.2.11">



<div _ngcontent-c0="">
  <img _ngcontent-c0="" class="favicon" src="favicon.ico">
  <div _ngcontent-c0="" class="main">
    <main _ngcontent-c0="" defaultoverlaytarget="">
      <div _ngcontent-c0="" data-unified-header="" tabindex="0">
        <app-top-nav _ngcontent-c0="" _nghost-c1=""><!----><nav _ngcontent-c1="" aria-label="Top Header" class="bx--top-nav" role="navigation">
  <div _ngcontent-c1="" class="bx--global-header__left-container">
    <a _ngcontent-c1="" class="brand-wrapper" href="/dashboard">
      <!----><div _ngcontent-c1="" class="logo-wrapper" style="background-color: rgb(15, 33, 46);">
        <img _ngcontent-c1="" class="logo default-logo" alt="Cloud Matrix Logo" src="assets/img/cm-logo.svg">
      </div>

      <!----><div _ngcontent-c1="" class="header-title">
        <h1 _ngcontent-c1="" class="bx--logo__text" title="Cloud Brokerage">
          Cloud Brokerage  </h1>
      </div>
    </a>
    <!----><ul _ngcontent-c1="" aria-hidden="false" class="bx--global-header__menu" data-global-header-menu="" role="menubar">

      
      <!----><li _ngcontent-c1="" class="orders-overflow-menu">    
        <span _ngcontent-c1="" aria-label="Orders Menu" class="bx--overflow-menu">  
            <a _ngcontent-c1="" class="bx--global-header__menu__item--link" href="javascript:void(0)" id="ordersLinkId" tabindex="0" title="Orders">Orders</a>
            <ul _ngcontent-c1="" class="bx--overflow-menu-options bx--overflow-menu--flip" id="orders-overflow-menu-container" tabindex="-1">
                <!----><li _ngcontent-c1="" class="bx--overflow-menu-options__option" id="approveOrderSubmenu" role="menuitem" title="Approve Orders">
                    <a _ngcontent-c1="" class="bx--overflow-menu-options__btn" href="/orders/approver-orders" id="approverOrdersLinkId" tabindex="0" title="Approve Orders">Approve Orders</a>
                </li>
                <!----><li _ngcontent-c1="" class="bx--overflow-menu-options__option" id="orderHistorySubmenu" role="menuitem" title="Order History">
                    <a _ngcontent-c1="" class="bx--overflow-menu-options__btn" href="/orders/my-orders" id="myordersLinkId" tabindex="0" title="Order History">Order History</a>
                </li>
            </ul>
          </span>
      </li> 

      <!----><li _ngcontent-c1="" role="menuitem">
        <a _ngcontent-c1="" class="bx--global-header__menu__item--link" href="/storeFront/main" id="catalogLinkId" tabindex="0" title="Catalog">Catalog</a>
      </li>

      <!----><li _ngcontent-c1="" role="menuitem">
        <a _ngcontent-c1="" class="bx--global-header__menu__item--link" href="/inventory" id="inventoryLinkId" tabindex="0" title="Inventory">Inventory</a>
      </li>

      <!----><li _ngcontent-c1="" role="menuitem">
        <a _ngcontent-c1="" class="bx--global-header__menu__item--link" href="/conversion" id="conversionLinkId" tabindex="0" title="Currency Conversion">Currency Conversion</a>
      </li>

      <!----><li _ngcontent-c1="" role="menuitem">
        <a _ngcontent-c1="" class="bx--global-header__menu__item--link" href="/budget" id="budgetLinkId" tabindex="0" title="Budget">Budget</a>
      </li>

      <!----><li _ngcontent-c1="" role="menuitem">
        <a _ngcontent-c1="" class="bx--global-header__menu__item--link" href="/catalogAdmin" id="catalogAdminLinkId" tabindex="0" title="Catalog Admin">Catalog Admin</a>
      </li>
      <!---->
    </ul>
  </div>

  <!----><div _ngcontent-c1="" class="bx--global-header__right-container">
    <!----><div _ngcontent-c1=""><!----><app-cart-menu _ngcontent-c1="" _nghost-c5=""><div _ngcontent-c5="" class="current-cart" id="selected-cart">
  <!---->
  <!---->
  <div _ngcontent-c5="" aria-label="Cart">
    <button _ngcontent-c5="" class="bx--cloud-header-list__btn" id="cart-btn" type="button">
      <img _ngcontent-c5="" alt="cart" class="cart-icon" src="/assets/img/cart.svg">
    </button>
    <div _ngcontent-c5="" aria-label="Overflow menu description" class="bx--overflow-menu">
      <ul _ngcontent-c5="" class="bx--overflow-menu-options bx--overflow-menu--flip" data-floating-menu-direction="bottom" tabindex="-1">
        <li _ngcontent-c5="" class="toolbar-menu__title">Current Cart</li>
        <li _ngcontent-c5="" class="bx--overflow-menu-options__option">
          <!---->
          <!----><span _ngcontent-c5="" class="bx--overflow-menu-options__btn">Empty</span>
        </li>
        <hr _ngcontent-c5="" class="bx--toolbar-menu__divider">
        <div _ngcontent-c5="" class="scroll-class">
          <li _ngcontent-c5="" class="toolbar-menu__title">Saved Carts</li>
          <!----><li _ngcontent-c5="" class="bx--overflow-menu-options__option">
            <button _ngcontent-c5="" class="bx--overflow-menu-options__btn" title="ordersbag7UAG">ordersbag7UAG</button>
          </li><li _ngcontent-c5="" class="bx--overflow-menu-options__option">
            <button _ngcontent-c5="" class="bx--overflow-menu-options__btn" title="ordersbagG0QV">ordersbagG0QV</button>
          </li><li _ngcontent-c5="" class="bx--overflow-menu-options__option">
            <button _ngcontent-c5="" class="bx--overflow-menu-options__btn" title="ordersbagM8ZL">ordersbagM8ZL</button>
          </li><li _ngcontent-c5="" class="bx--overflow-menu-options__option">
            <button _ngcontent-c5="" class="bx--overflow-menu-options__btn" title="ordersbagNF64">ordersbagNF64</button>
          </li><li _ngcontent-c5="" class="bx--overflow-menu-options__option">
            <button _ngcontent-c5="" class="bx--overflow-menu-options__btn" title="testcart">testcart</button>
          </li><li _ngcontent-c5="" class="bx--overflow-menu-options__option">
            <button _ngcontent-c5="" class="bx--overflow-menu-options__btn" title="testcart">testcart</button>
          </li><li _ngcontent-c5="" class="bx--overflow-menu-options__option">
            <button _ngcontent-c5="" class="bx--overflow-menu-options__btn" title="testcart">testcart</button>
          </li><li _ngcontent-c5="" class="bx--overflow-menu-options__option">
            <button _ngcontent-c5="" class="bx--overflow-menu-options__btn" title="testcart">testcart</button>
          </li><li _ngcontent-c5="" class="bx--overflow-menu-options__option">
            <button _ngcontent-c5="" class="bx--overflow-menu-options__btn" title="testcart">testcart</button>
          </li>
          <!---->
        </div>
      </ul>
    </div>
  </div>
</div>
</app-cart-menu></div>
    <help-link _ngcontent-c1="" _nghost-c6="">
    <button _ngcontent-c6="" class="bx--cloud-header-list__btn" id="help-link-btn" type="button">
      <!----><img _ngcontent-c6="" class="help-icon" src="/assets/img/help.svg" title="Help">
    </button>
  </help-link>
    <app-sub-menu-nav _ngcontent-c1="" _nghost-c7=""><div _ngcontent-c7="" id="profile">
    <div _ngcontent-c7="" aria-label="Profile menu">
        <button _ngcontent-c7="" class="bx--cloud-header-list__btn" id="user_icon_id" type="button">
            <img _ngcontent-c7="" alt="user" class="user-icon" src="/assets/img/user.svg">
        </button>
        <div _ngcontent-c7="" aria-label="Profile Menu" class="bx--overflow-menu">
            <ul _ngcontent-c7="" class="bx--overflow-menu-options bx--overflow-menu--flip" tabindex="-1">
                <li _ngcontent-c7="" class="bx--overflow-menu-options__option" title="BuyerQATEAM
e2e_buyerteam
e2e_finapproval
e2e_operator
e2e_purchaser
e2e_team1
e2e_team1_core1
e2e_techapproval
e2esvtapi
e2esvtapi_purchaser
e2esvtapi-TEAM-SETUP-ADMIN
e2esvtapiCatalogAdmin
e2esvtapiSupport
TEAM1">
                    <button _ngcontent-c7="" class="bx--overflow-menu-options__btn" data-floating-menu-primary-focus="">cloud.brokertest@gmail.com/ e2e_operator</button>
                </li>
                <!----><li _ngcontent-c7="" class="bx--overflow-menu-options__option" id="accountsSubMenu" role="menuitem" title="Accounts">
                    <button _ngcontent-c7="" class="bx--overflow-menu-options__btn" id="accountsSubMenuButton">Accounts</button>
                </li>
                <!---->
                <!----><li _ngcontent-c7="" class="bx--overflow-menu-options__option" id="userAccessSubMenu" role="menuitem">
                    <button _ngcontent-c7="" class="bx--overflow-menu-options__btn" id="userAccessSubMenuButton">User Access</button>
                </li>
                <!----><li _ngcontent-c7="" class="bx--overflow-menu-options__option" id="apiKeySubMenu" role="menuitem">
                    <button _ngcontent-c7="" class="bx--overflow-menu-options__btn" id="apiKeySubMenuButton">API Key</button>
                </li>
                <!----> 
                <li _ngcontent-c7="" class="bx--overflow-menu-options__option bx--overflow-menu-options__option--danger" id="logoutSubMenu">
                    <button _ngcontent-c7="" class="bx--overflow-menu-options__btn" id="logoutSubMenuButton">Logout</button>
                </li>
            </ul>
        </div>
    </div>
</div>
</app-sub-menu-nav>
 </div>
</nav>
<app-apikey-model _ngcontent-c1="" apikey="apiKey" _nghost-c8=""><carbon-modal _ngcontent-c8="" id="api-key-modal-id" _nghost-c10="">
    
    <div _ngcontent-c10="" class="bx--modal" tabindex="-1">
      <div _ngcontent-c10="" class="bx--modal-container">
        <div _ngcontent-c10="" class="bx--modal-header">
          <h2 _ngcontent-c10="" class="bx--modal-header__heading">API Key</h2>
          <!----><button _ngcontent-c10="" class="bx--modal-close" type="button" id="close-btn_api-key-modal">
            <carbon-icon _ngcontent-c10="" class="" name="close" _nghost-c12="" id="close-icon_api-key-modal">
      
      <svg _ngcontent-c12="" class="bx--modal-close__icon" height="10" width="10" viewBox="0 0 10 10">
        <!----><!---->
        <!----><!---->
        <path _ngcontent-c12="" d="M6.32 5L10 8.68 8.68 10 5 6.32 1.32 10 0 8.68 3.68 5 0 1.32 1.32 0 5 3.68 8.68 0 10 1.32 6.32 5z"></path>
        
        
      </svg>
  </carbon-icon>
          </button>
        </div>

        <div _ngcontent-c10="" class="bx--modal-content">
          
          <div _ngcontent-c8="" modal-body="">
    <!---->
    <!---->
    <carbon-loading _ngcontent-c8="" _nghost-c3="">
    
  <!----></carbon-loading>
    <!----><div _ngcontent-c8="">
      <div _ngcontent-c8="" class="bx--row">
        <!---->

        <!----><div _ngcontent-c8="" class="bx--col-xs-6">
          <carbon-button _ngcontent-c8="" id="generate-api-key-button" style="padding-left: 0.5rem" type="primary" title="Generate API Key">
    <button class="bx--btn bx--btn--primary" id="button-generate-api-key-button">
       Generate API Key
          
    </button>
  </carbon-button>
        </div>
      </div>
      <!---->
      <br _ngcontent-c8="">
      <!---->
    </div>
    <!---->

    <!---->
  </div>
        </div>

        <!---->
      </div>
    </div>
  </carbon-modal>
</app-apikey-model>
</app-top-nav>
        <app-top-header-controller _ngcontent-c0="" _nghost-c2=""><!----><div _ngcontent-c2="" class="bx--unified-header bx--unified-header--apps" data-unified-header="" tabindex="0">
  <!----><app-top-header _ngcontent-c2="" _nghost-c9=""><!----><header _ngcontent-c9="" class="bx--global-header" role="banner">
  <div _ngcontent-c9="" class="left">
    <!----><!----><!----><!----><!----><!----><!----><!----><!---->
  </div>
  <div _ngcontent-c9="" class="right">
    
  </div>
</header>
</app-top-header>
</div>
</app-top-header-controller>
      </div>
      <carbon-loading _ngcontent-c0="" _nghost-c3="">
    
  <!----></carbon-loading>
      <router-outlet _ngcontent-c0=""></router-outlet><app-additional-params _nghost-c36=""><carbon-loading _ngcontent-c36="" _nghost-c3="">
    
  <!----></carbon-loading>

<carbon-notification _ngcontent-c36="" appearance="toast" type="info" _nghost-c11="" class=" bx--toast-notification bx--toast-notification--info " role="alert">
    
    <!----><div _ngcontent-c11="" class="bx--toast-notification__details">
      <!---->
      <!----><div _ngcontent-c11="" class="bx--toast-notification__details">
        <p _ngcontent-c11="" class="bx--toast-notification__title"></p>
        <p _ngcontent-c11="" class="bx--toast-notification__subtitle"></p>
        <p _ngcontent-c11="" class="bx--toast-notification__caption"></p>
      </div>
    </div>
    <!----><button _ngcontent-c11="" type="button" class="bx--toast-notification__close-button">
      <carbon-icon _ngcontent-c11="" name="close" _nghost-c12="" class="">
      
      <svg _ngcontent-c12="" class="bx--toast-notification__close-icon" height="10" width="10" viewBox="0 0 10 10">
        <!----><!---->
        <!----><!---->
        <path _ngcontent-c12="" d="M6.32 5L10 8.68 8.68 10 5 6.32 1.32 10 0 8.68 3.68 5 0 1.32 1.32 0 5 3.68 8.68 0 10 1.32 6.32 5z"></path>
        
        
      </svg>
  </carbon-icon>
    </button>
  </carbon-notification>

<div _ngcontent-c36="" class="bx--unified-header bx--unified-header--apps" data-unified-header="" tabindex="0">
  <app-top-header _ngcontent-c36="" _nghost-c9=""><!----><header _ngcontent-c9="" class="bx--global-header" role="banner">
  <div _ngcontent-c9="" class="left">
    <div _ngcontent-c36="" left="">
      <app-header-left _ngcontent-c36="" _nghost-c24=""><div _ngcontent-c24="" class="header-row">
  <div _ngcontent-c24="" class="bx--breadcrumb">
    <div _ngcontent-c24="" class="bx--breadcrumb-item">
      <!----><a _ngcontent-c24="" class="bx--link" href="/storeFront/main">Catalog</a>
      <!---->
    </div>
    <!----><div _ngcontent-c24="" class="bx--breadcrumb-item">
      <a _ngcontent-c24="" class="bx--link" style="cursor:pointer">DETAILS</a>
    </div>
    <div _ngcontent-c24="" class="bx--breadcrumb-item">
      <!----><span _ngcontent-c24="">PLACE ORDER</span>
      <!---->
    </div>
  </div>
</div>
<div _ngcontent-c24="" class="bottom-row" id="main-params_service-order">
  <!----><span _ngcontent-c24="" class="configure-service">Configure Service </span>
  <!---->
</div>
</app-header-left>
    </div>
  </div>
  <div _ngcontent-c9="" class="right">
    <div _ngcontent-c36="" right="">

      <store-cart _ngcontent-c36="" id="additional-params_store-cart">
        <div _ngcontent-c36="" class="bx--button-group">
          <carbon-button _ngcontent-c36="" id="cancel-button-additionalParams" size="large" type="secondary" title="Cancel">
    <button class="bx--btn bx--btn--secondary" id="button-cancel-button-additionalParams">
      
            Cancel
          
    </button>
  </carbon-button>

          <carbon-button _ngcontent-c36="" id="previous-button-additionalParams" size="large" type="secondary" title="Previous">
    <button class="bx--btn bx--btn--secondary" id="button-previous-button-additionalParams">
      
            Previous
          
    </button>
  </carbon-button>

          <carbon-button _ngcontent-c36="" id="next-button-additionalParams" size="large" type="primary" title="Next">
    <button class="bx--btn bx--btn--primary" id="button-next-button-additionalParams" disabled="">
      
            Next
          
    </button>
  </carbon-button>
        </div>

      </store-cart>

    </div>
  </div>
</header>
</app-top-header>
</div>

<service-progress _ngcontent-c36="" id="additional-params_service-progress" _nghost-c25=""><div _ngcontent-c25="" class="service-progress">
    <div _ngcontent-c25="" class="left">
        <div _ngcontent-c25="" class="left-progress">
            <div _ngcontent-c25="" class="circle-img">
                <img _ngcontent-c25="" title="Upload Image" src="/assets/img/icon-application.svg" alt="Amazon">
            </div>
        </div>
        <div _ngcontent-c25="" class="right-progress">
            <tooltip-wrapper _ngcontent-c25="" id="service-progress_tooltip-wrapper" tooltipdirection="bottom" _nghost-c21="">
    
    <div _ngcontent-c21="">
      <!---->
                    <span _ngcontent-c25="" class="blueprint-name" id="service-progress_blueprint-name">Simple Notification Service (SNS)</span>
                
      <carbon-tooltip _ngcontent-c21="" class="tooltip-content" _nghost-c22="">
    
    <div _ngcontent-c22="" class="bx--tooltip" id="tooltip-81" data-floating-menu-direction="bottom">
      <!---->
      <p _ngcontent-c22="" class="bx--tooltip-overlow">
        
        <!---->
                    <span _ngcontent-c25="" class="blueprint-name-tooltip"> Simple Notification Service (SNS) </span>
                
      
      </p>
    </div>
  </carbon-tooltip>
    </div>
  </tooltip-wrapper>
        </div>
    </div>
    <div _ngcontent-c25="" class="progress-indicator" style="margin-left: 4.6875rem;">
        
  <carbon-progress-indicator _ngcontent-c36="" id="additional-params_progress-indicator">
  <ul class="bx--progress" data-progress="" data-progress-current="">
    <!----><carbon-progress-indicator-item class="bx--progress-step" _nghost-c32="" style="min-width: 5.5rem;"><li _ngcontent-c32="" class="bx--progress-step--complete">
    <svg _ngcontent-c32="" height="24px" viewBox="0 0 24 24" width="24px" class="cursor-class cursor-class:hover">
        <circle _ngcontent-c32="" cx="12" cy="12" r="12" style="stroke: rgb(61, 112, 178); animation: 0.75s ease 0s 1 normal none running circle;"></circle>
        <!---->
        <!----><polygon _ngcontent-c32="" class="check" points="10.3 13.6 7.7 11 6.3 12.4 10.3 16.4 17.8 9 16.4 7.6" style="stroke: rgb(61, 112, 178); fill: rgb(61, 112, 178);"></polygon>
        <!---->
    </svg>
    <p _ngcontent-c32="" class="bx--progress-label" style="font-size: 0.9rem; color: rgb(61, 112, 178);">Main Parameters</p>
    <p _ngcontent-c32="" class="bx--progress-label" style="color: rgb(61, 112, 178); font-size: 0.9rem;"></p>
    <p _ngcontent-c32="" class="bx--progress-label" style="color: rgb(61, 112, 178); font-size: 0.9rem;"></p>
    <!---->
</li></carbon-progress-indicator-item><carbon-progress-indicator-item class="bx--progress-step" _nghost-c32="" style="min-width: 5.5rem;"><li _ngcontent-c32="" class="bx--progress-step--current">
    <svg _ngcontent-c32="" height="24px" viewBox="0 0 24 24" width="24px" class="cursor-class cursor-class:hover">
        <circle _ngcontent-c32="" cx="12" cy="12" r="12" style="stroke: rgb(65, 120, 154);"></circle>
        <!----><circle _ngcontent-c32="" cx="12" cy="12" r="6" style="stroke: rgb(65, 120, 154); fill: rgb(65, 120, 154); transition: fill 1s ease 0s, stroke 1s ease 0s;"></circle>
        <!---->
        <!---->
    </svg>
    <p _ngcontent-c32="" class="bx--progress-label" style="color: rgb(65, 120, 154); font-size: 0.9rem;">Configure Region</p>
    <p _ngcontent-c32="" class="bx--progress-label" style="color: rgb(65, 120, 154); font-size: 0.9rem;"></p>
    <p _ngcontent-c32="" class="bx--progress-label" style="color: rgb(65, 120, 154); font-size: 0.9rem;"></p>
    <!----><span _ngcontent-c32="" class="bx--progress-line" style="background: rgb(65, 120, 154); opacity: 1; transition: background 1s ease 0s, opacity 1s ease 0s;"></span>
</li></carbon-progress-indicator-item><carbon-progress-indicator-item class="bx--progress-step" _nghost-c32="" style="min-width: 5.5rem;"><li _ngcontent-c32="" class="bx--progress-step--incomplete">
    <svg _ngcontent-c32="" height="24px" viewBox="0 0 24 24" width="24px">
        <circle _ngcontent-c32="" cx="12" cy="12" r="12" style="stroke: rgb(69, 127, 129);"></circle>
        <!---->
        <!---->
        <!---->
    </svg>
    <p _ngcontent-c32="" class="bx--progress-label" style="font-size: 0.9rem;">Topic Information</p>
    <p _ngcontent-c32="" class="bx--progress-label" style="color: rgb(69, 127, 129); font-size: 0.9rem;"></p>
    <p _ngcontent-c32="" class="bx--progress-label" style="color: rgb(69, 127, 129); font-size: 0.9rem;"></p>
    <!----><span _ngcontent-c32="" class="bx--progress-line" style="transition: background 1s ease 0s, opacity 1s ease 0s;"></span>
</li></carbon-progress-indicator-item><carbon-progress-indicator-item class="bx--progress-step" _nghost-c32="" style="min-width: 5.5rem;"><li _ngcontent-c32="" class="bx--progress-step--incomplete">
    <svg _ngcontent-c32="" height="24px" viewBox="0 0 24 24" width="24px">
        <circle _ngcontent-c32="" cx="12" cy="12" r="12" style="stroke: rgb(73, 135, 105);"></circle>
        <!---->
        <!---->
        <!---->
    </svg>
    <p _ngcontent-c32="" class="bx--progress-label" style="font-size: 0.9rem;">Subscription Details</p>
    <p _ngcontent-c32="" class="bx--progress-label" style="color: rgb(73, 135, 105); font-size: 0.9rem;"></p>
    <p _ngcontent-c32="" class="bx--progress-label" style="color: rgb(73, 135, 105); font-size: 0.9rem;"></p>
    <!----><span _ngcontent-c32="" class="bx--progress-line" style="transition: background 1s ease 0s, opacity 1s ease 0s;"></span>
</li></carbon-progress-indicator-item><carbon-progress-indicator-item class="bx--progress-step" _nghost-c32="" style="min-width: 5.5rem;"><li _ngcontent-c32="" class="bx--progress-step--incomplete">
    <svg _ngcontent-c32="" height="24px" viewBox="0 0 24 24" width="24px">
        <circle _ngcontent-c32="" cx="12" cy="12" r="12" style="stroke: rgb(77, 142, 80);"></circle>
        <!---->
        <!---->
        <!---->
    </svg>
    <p _ngcontent-c32="" class="bx--progress-label" style="font-size: 0.9rem;">Review Order</p>
    <p _ngcontent-c32="" class="bx--progress-label" style="color: rgb(77, 142, 80); font-size: 0.9rem;"></p>
    <p _ngcontent-c32="" class="bx--progress-label" style="color: rgb(77, 142, 80); font-size: 0.9rem;"></p>
    <!----><span _ngcontent-c32="" class="bx--progress-line" style="transition: background 1s ease 0s, opacity 1s ease 0s;"></span>
</li></carbon-progress-indicator-item>
  </ul></carbon-progress-indicator>

    </div>
</div>
</service-progress>

<div _ngcontent-c36="" class="content">
  <div _ngcontent-c36="" class="left">
    <div _ngcontent-c36="" class="left-container">
      <div _ngcontent-c36="" class="description-section">
        <storefront-service-left-desc _ngcontent-c36="" _nghost-c26="">
<!----><div _ngcontent-c26="" class="description">
  <p _ngcontent-c26=""> Simple Notification Service (SNS) is a flexible, fully managed pub/sub messaging and mobile notifications service for coordinating the delivery of messages to subscribing endpoints and clients. </p>
</div>

<!---->

<carbon-modal _ngcontent-c26="" _nghost-c10="">
    
    <div _ngcontent-c10="" class="bx--modal" tabindex="-1">
      <div _ngcontent-c10="" class="bx--modal-container">
        <div _ngcontent-c10="" class="bx--modal-header">
          <h2 _ngcontent-c10="" class="bx--modal-header__heading">Modal title test</h2>
          <!----><button _ngcontent-c10="" class="bx--modal-close" type="button" id="close-btn_price-modal">
            <carbon-icon _ngcontent-c10="" class="" name="close" _nghost-c12="" id="close-icon_price-modal">
      
      <svg _ngcontent-c12="" class="bx--modal-close__icon" height="10" width="10" viewBox="0 0 10 10">
        <!----><!---->
        <!----><!---->
        <path _ngcontent-c12="" d="M6.32 5L10 8.68 8.68 10 5 6.32 1.32 10 0 8.68 3.68 5 0 1.32 1.32 0 5 3.68 8.68 0 10 1.32 6.32 5z"></path>
        
        
      </svg>
  </carbon-icon>
          </button>
        </div>

        <div _ngcontent-c10="" class="bx--modal-content">
          
          <div _ngcontent-c26="" modal-body="">Table data</div>
        </div>

        <!---->
      </div>
    </div>
  </carbon-modal>
</storefront-service-left-desc>
      </div>
      <!---->
    </div>
  </div>
  <div _ngcontent-c36="" class="right">
    <!---->
    <!----><div _ngcontent-c36="">
      <!---->
    </div>
    <!----><div _ngcontent-c36="" class="container-main">
      <!---->

      <!---->

      <!---->
      <dynamic-form _ngcontent-c36="" id="additional-params_dynamic-form" _nghost-c37=""><form _ngcontent-c37="" class="dynamic-form ng-untouched ng-pristine ng-invalid" novalidate="">
  <!----><!----><form-select _nghost-c38=""><div _ngcontent-c38="" class="form-field ng-untouched ng-pristine ng-invalid">

  <carbon-dropdown _ngcontent-c38="" class="form-field-item ng-untouched ng-pristine ng-invalid" _nghost-c30="" title="AWS Region is a separate geographic area. Each AWS Region has multiple, isolated locations known as Availability Zones."><div _ngcontent-c30="" class="bx--form-item" id="dropdown-scroll">
    <!----><div _ngcontent-c30=""><!----><span _ngcontent-c30="" class="required"> * </span>
        <label _ngcontent-c30="" class="bx--label">AWS Region</label>
        <!---->
    </div>
    <ul _ngcontent-c30="" class="bx--dropdown" tabindex="0" id="bx--dropdown-single-parent_AWS::Region">
        <li _ngcontent-c30="" class="bx--dropdown-text">
            Choose an option
        </li>
        <!----><!---->
            <!---->
        
        <!----><carbon-icon _ngcontent-c30="" class="" name="caret--down" _nghost-c12="">
      
      <svg _ngcontent-c12="" class="bx--dropdown__arrow" height="5" width="10" viewBox="0 0 10 5">
        <!----><!---->
        <!----><!---->
        <path _ngcontent-c12="" d="M0 0l5 4.998L10 0z"></path>
        
        
      </svg>
  </carbon-icon>
        <li _ngcontent-c30="">
            <ul _ngcontent-c30="" class="bx--dropdown-list" tabindex="0">
                <!----><carbon-dropdown-option _ngcontent-c30="" _nghost-c33="">
    
    <li _ngcontent-c33="" class="bx--dropdown-item" tabindex="0">
      <a _ngcontent-c33="" class="bx--dropdown-link" tabindex="0" id="dropdown-option_AWS::Region_apnortheast1">
        
        <!---->
        
                    ap-northeast-1
                
      </a>
    </li>
  </carbon-dropdown-option><carbon-dropdown-option _ngcontent-c30="" _nghost-c33="">
    
    <li _ngcontent-c33="" class="bx--dropdown-item" tabindex="0">
      <a _ngcontent-c33="" class="bx--dropdown-link" tabindex="0" id="dropdown-option_AWS::Region_apnortheast2">
        
        <!---->
        
                    ap-northeast-2
                
      </a>
    </li>
  </carbon-dropdown-option><carbon-dropdown-option _ngcontent-c30="" _nghost-c33="">
    
    <li _ngcontent-c33="" class="bx--dropdown-item" tabindex="0">
      <a _ngcontent-c33="" class="bx--dropdown-link" tabindex="0" id="dropdown-option_AWS::Region_apsouth1">
        
        <!---->
        
                    ap-south-1
                
      </a>
    </li>
  </carbon-dropdown-option><carbon-dropdown-option _ngcontent-c30="" _nghost-c33="">
    
    <li _ngcontent-c33="" class="bx--dropdown-item" tabindex="0">
      <a _ngcontent-c33="" class="bx--dropdown-link" tabindex="0" id="dropdown-option_AWS::Region_apsoutheast1">
        
        <!---->
        
                    ap-southeast-1
                
      </a>
    </li>
  </carbon-dropdown-option><carbon-dropdown-option _ngcontent-c30="" _nghost-c33="">
    
    <li _ngcontent-c33="" class="bx--dropdown-item" tabindex="0">
      <a _ngcontent-c33="" class="bx--dropdown-link" tabindex="0" id="dropdown-option_AWS::Region_apsoutheast2">
        
        <!---->
        
                    ap-southeast-2
                
      </a>
    </li>
  </carbon-dropdown-option><carbon-dropdown-option _ngcontent-c30="" _nghost-c33="">
    
    <li _ngcontent-c33="" class="bx--dropdown-item" tabindex="0">
      <a _ngcontent-c33="" class="bx--dropdown-link" tabindex="0" id="dropdown-option_AWS::Region_cacentral1">
        
        <!---->
        
                    ca-central-1
                
      </a>
    </li>
  </carbon-dropdown-option><carbon-dropdown-option _ngcontent-c30="" _nghost-c33="">
    
    <li _ngcontent-c33="" class="bx--dropdown-item" tabindex="0">
      <a _ngcontent-c33="" class="bx--dropdown-link" tabindex="0" id="dropdown-option_AWS::Region_eucentral1">
        
        <!---->
        
                    eu-central-1
                
      </a>
    </li>
  </carbon-dropdown-option><carbon-dropdown-option _ngcontent-c30="" _nghost-c33="">
    
    <li _ngcontent-c33="" class="bx--dropdown-item" tabindex="0">
      <a _ngcontent-c33="" class="bx--dropdown-link" tabindex="0" id="dropdown-option_AWS::Region_eunorth1">
        
        <!---->
        
                    eu-north-1
                
      </a>
    </li>
  </carbon-dropdown-option><carbon-dropdown-option _ngcontent-c30="" _nghost-c33="">
    
    <li _ngcontent-c33="" class="bx--dropdown-item" tabindex="0">
      <a _ngcontent-c33="" class="bx--dropdown-link" tabindex="0" id="dropdown-option_AWS::Region_euwest1">
        
        <!---->
        
                    eu-west-1
                
      </a>
    </li>
  </carbon-dropdown-option><carbon-dropdown-option _ngcontent-c30="" _nghost-c33="">
    
    <li _ngcontent-c33="" class="bx--dropdown-item" tabindex="0">
      <a _ngcontent-c33="" class="bx--dropdown-link" tabindex="0" id="dropdown-option_AWS::Region_euwest2">
        
        <!---->
        
                    eu-west-2
                
      </a>
    </li>
  </carbon-dropdown-option><carbon-dropdown-option _ngcontent-c30="" _nghost-c33="">
    
    <li _ngcontent-c33="" class="bx--dropdown-item" tabindex="0">
      <a _ngcontent-c33="" class="bx--dropdown-link" tabindex="0" id="dropdown-option_AWS::Region_euwest3">
        
        <!---->
        
                    eu-west-3
                
      </a>
    </li>
  </carbon-dropdown-option><carbon-dropdown-option _ngcontent-c30="" _nghost-c33="">
    
    <li _ngcontent-c33="" class="bx--dropdown-item" tabindex="0">
      <a _ngcontent-c33="" class="bx--dropdown-link" tabindex="0" id="dropdown-option_AWS::Region_saeast1">
        
        <!---->
        
                    sa-east-1
                
      </a>
    </li>
  </carbon-dropdown-option><carbon-dropdown-option _ngcontent-c30="" _nghost-c33="">
    
    <li _ngcontent-c33="" class="bx--dropdown-item" tabindex="0">
      <a _ngcontent-c33="" class="bx--dropdown-link" tabindex="0" id="dropdown-option_AWS::Region_useast1">
        
        <!---->
        
                    us-east-1
                
      </a>
    </li>
  </carbon-dropdown-option><carbon-dropdown-option _ngcontent-c30="" _nghost-c33="">
    
    <li _ngcontent-c33="" class="bx--dropdown-item" tabindex="0">
      <a _ngcontent-c33="" class="bx--dropdown-link" tabindex="0" id="dropdown-option_AWS::Region_useast2">
        
        <!---->
        
                    us-east-2
                
      </a>
    </li>
  </carbon-dropdown-option><carbon-dropdown-option _ngcontent-c30="" _nghost-c33="">
    
    <li _ngcontent-c33="" class="bx--dropdown-item" tabindex="0">
      <a _ngcontent-c33="" class="bx--dropdown-link" tabindex="0" id="dropdown-option_AWS::Region_uswest1">
        
        <!---->
        
                    us-west-1
                
      </a>
    </li>
  </carbon-dropdown-option><carbon-dropdown-option _ngcontent-c30="" _nghost-c33="">
    
    <li _ngcontent-c33="" class="bx--dropdown-item" tabindex="0">
      <a _ngcontent-c33="" class="bx--dropdown-link" tabindex="0" id="dropdown-option_AWS::Region_uswest2">
        
        <!---->
        
                    us-west-2
                
      </a>
    </li>
  </carbon-dropdown-option>
                <!----><!---->
                    <!---->
                
                
  
            </ul>
        </li>
    </ul>
    <!---->
</div></carbon-dropdown>

  <!---->
  <!----><div _ngcontent-c38="" class="tooltip" style="margin-top: 2.5rem">
    <carbon-icon _ngcontent-c38="" class="" name="info--glyph" _nghost-c12="">
      
      <svg _ngcontent-c12="" class="info-icon" height="16" width="16" viewBox="0 0 16 16">
        <!----><!---->
        <!----><!---->
        <path _ngcontent-c12="" d="M8 0C3.6 0 0 3.6 0 8s3.6 8 8 8 8-3.6 8-8-3.6-8-8-8zm0 4c.6 0 1 .4 1 1s-.4 1-1 1-1-.4-1-1 .4-1 1-1zm2 8H6v-1h1V8H6V7h3v4h1v1z"></path>
        
        
      </svg>
  </carbon-icon>
    <!----><span _ngcontent-c38="" class="tooltiptext">
      AWS Region is a separate geographic area. Each AWS Region has multiple, isolated locations known as Availability Zones.
    </span>
  </div>
</div>
</form-select>
  
</form>
</dynamic-form>
    </div>
  </div>
</div>

<carbon-modal _ngcontent-c36="" modalid="additional-params-order-cancel-modal" _nghost-c10="">
    
    <div _ngcontent-c10="" class="bx--modal" tabindex="-1">
      <div _ngcontent-c10="" class="bx--modal-container">
        <div _ngcontent-c10="" class="bx--modal-header">
          <h2 _ngcontent-c10="" class="bx--modal-header__heading">Order Cancel Confirmation</h2>
          <!----><button _ngcontent-c10="" class="bx--modal-close" type="button" id="close-btn_additional-params-order-cancel-modal">
            <carbon-icon _ngcontent-c10="" class="" name="close" _nghost-c12="" id="close-icon_additional-params-order-cancel-modal">
      
      <svg _ngcontent-c12="" class="bx--modal-close__icon" height="10" width="10" viewBox="0 0 10 10">
        <!----><!---->
        <!----><!---->
        <path _ngcontent-c12="" d="M6.32 5L10 8.68 8.68 10 5 6.32 1.32 10 0 8.68 3.68 5 0 1.32 1.32 0 5 3.68 8.68 0 10 1.32 6.32 5z"></path>
        
        
      </svg>
  </carbon-icon>
          </button>
        </div>

        <div _ngcontent-c10="" class="bx--modal-content">
          
          <div _ngcontent-c36="" modal-body="">
    <p _ngcontent-c36="">
      Do you really want to cancel this order?
    </p>
  </div>
        </div>

        <!----><div _ngcontent-c10="" class="bx--modal-footer">
          <div _ngcontent-c36="" modal-footer="">

    <carbon-button _ngcontent-c36="" id="additional-params-order-cancel-modal_carbon-button_no" size="small" type="secondary">
    <button class="bx--btn bx--btn--secondary bx--btn--sm" id="button-additional-params-order-cancel-modal_carbon-button_no">
      
      NO
    
    </button>
  </carbon-button>

    <carbon-button _ngcontent-c36="" id="additional-params-order-cancel-modal_carbon-button_yes" size="small" type="primary">
    <button class="bx--btn bx--btn--primary bx--btn--sm" id="button-additional-params-order-cancel-modal_carbon-button_yes">
      
      YES
    
    </button>
  </carbon-button>

  </div>
        </div>
      </div>
    </div>
  </carbon-modal>
</app-additional-params>
    </main>
  </div>
</div>

<app-session-timeout _ngcontent-c0="" _nghost-c4=""><carbon-modal _ngcontent-c4="" _nghost-c10="">
    
    <div _ngcontent-c10="" class="bx--modal" tabindex="-1">
      <div _ngcontent-c10="" class="bx--modal-container">
        <div _ngcontent-c10="" class="bx--modal-header">
          <h2 _ngcontent-c10="" class="bx--modal-header__heading">Session Time Out</h2>
          <!---->
        </div>

        <div _ngcontent-c10="" class="bx--modal-content">
          
          <div _ngcontent-c4="" modal-body="">
    <p _ngcontent-c4="">
      Your session will expire in {{ countdownTime }} seconds due to inactivity. Do you want to continue your session?
    </p>
  </div>
        </div>

        <!----><div _ngcontent-c10="" class="bx--modal-footer">
          <div _ngcontent-c4="" modal-footer="">
    <carbon-button _ngcontent-c4="" id="session-time-out-modal_carbon-button_continue" size="small" type="primary">
    <button class="bx--btn bx--btn--primary bx--btn--sm" id="button-session-time-out-modal_carbon-button_continue">
      
      Continue Session
    
    </button>
  </carbon-button>
  </div>
        </div>
      </div>
    </div>
  </carbon-modal>
</app-session-timeout>
</app-root>
    </div>
    <script src="properties.js"></script>
  <script type="text/javascript" src="runtime.55c17432536a23aa3ca9.js"></script><script type="text/javascript" src="polyfills.7f308ed5484912b9f63e.js"></script><script type="text/javascript" src="main.4ebc94db6a486dc9a99a.js"></script>

<!-- Last commit hash: cc587df5ffb65e4af08c078a5525cb8dac4aa5b5 -->
</body></html>
"""


def _get_text_from(soup, *args, **kwargs):
    text_list = []
    for x in soup.find_all(*args, **kwargs):
        text = ' '.join(x.get_text().strip().splitlines())
        if text and not re.search(r'[-!$%^&*()_+|~=`{}\[\]:";\'<>?,.\/0-9]+', text):
            text_list.append(text)
    return text_list


def html_to_soup(html, decompose_list=None):
    decompose_list = decompose_list if decompose_list else []
    soup = BeautifulSoup(html, 'html.parser')
    soup_body = soup.find('body')
    for d in decompose_list:
        elements = soup_body.find_all(d[0], d[1])
        for element in elements:
            element.decompose()
    return soup_body


def scrap_pages(soup, ignore_list=None):
    ignore_list = ignore_list if ignore_list else []

    def filter_ignore(items):
        return filter(lambda x: not any(ig in x for ig in ignore_list), items)
    phrases = []
    tags = ['label', 'a', 'button', 'span']
    for tag in tags:
        phrases += filter_ignore(_get_text_from(soup, tag))
    return phrases
    
class HtmlPhrase:
    def __init__(self, page_name, expected_language, text_list):
      self.page_name = page_name
      self.expected_language = expected_language
      self.text_list = text_list


class HtmlPhrases:
    def __init__(self, name, html_phrases):
        self.name = name
        self.html_phrases = html_phrases

    def add_html_phrase(self, page_name, expected_language, text_list):
        self.html_phrases.append(HtmlPhrase(page_name, expected_language, text_list))

    def to_csv(self):
        with open(f'{self.name}.csv', 'wb') as file:
            file.write(b'WebpageLink,ExpectedLanguage,Text\n')
            for phrase in self.html_phrases:
                file.writelines([f'{phrase.page_name},{phrase.expected_language},{x}\n'.encode() for x in phrase.text_list])


def sample(environment, language_code_list):
    test_results = order_pool_executor(environment, language_code_list, threads=True)
    ignores = [
        'cloud.brokertest@gmail.com/ e2e_operator',
        'admin gmail',
        'Azure',
        'Amazon',
        'Cloud Brokerage',
        'Google',
        'IBM',
        'ICD',
        'Test',
        'VRA',
        'API'
    ]
    nav_decomposes = [
        ['div', {'aria-label': 'Cart'}],
        ['a', {'class': 'bx--dropdown-link'}]
    ]
    review_order_decomposes = [
        ['div', {'class': 'order-summary-stats'}]
    ]
    review_order_decomposes += nav_decomposes
    html_phrases = []
    for result in test_results:
        for page in result[2]:
            page_name = page[0]
            html = page[1]
            soup = html_to_soup(html, review_order_decomposes)
            text_list = scrap_pages(soup, ignores)
            if page_name == 'Add Conversion Rate page':
                html_phrases.append(HtmlPhrase(page_name, result[0], text_list))
    HtmlPhrases('2019 hackathon example', html_phrases).to_csv()


if __name__ == '__main__':
    sample('cb-api-auto-test-release', ["en", "es", "de", "zh-CN"])
