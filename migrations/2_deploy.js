// migrations/2_deploy.js
// SPDX-License-Identifier: MIT
const cic = artifacts.require("cic");

module.exports = function(deployer) {
  deployer.deploy(cic);
};
