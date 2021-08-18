// migrations/2_deploy.js
// SPDX-License-Identifier: MIT
const Lottery = artifacts.require("Lottery");

module.exports = function(deployer) {
  deployer.deploy(Lottery);
};
