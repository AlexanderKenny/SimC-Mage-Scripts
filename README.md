Combination scripts and info dump for mages in World of Warcraft

# Folder Layout
## Combination Scripts
**Conduit Combinations** Generates combinations of all soulbind paths for a given soulbind and conduit level.<br/>
**Talent Combinations** Generates combinations of all talents for a given spec.<br/>
## Dump
### Input
**Base** Base spec profiles for all sims. The various combinations will be built on top of these.<br/>
**Cov** Full soulbind combination inputs. Broken out by rank of conduits (R#) then spec/soulbind.<br/>
**Talents** Full talent combination inputs. Broken out by spec. Inputs generated using Combination Scripts\Talent Combinations
### Output
**Cov** Full soulbind combinations. Broken out by targets (#T) then rank of conduits (R#) then finally spec/soulbind. Inputs generated with Combination Scripts\Conduit Combinations<br/>
**Talents** Full talent combinations. Broken out by targets (#T). Each spec includes a base (no covenant) output as well as an output for each covenant (ability only no soulbinds). Inputs generated using Combination Scripts\Talent Combinations<br/>

## Update Scripts
Contains personal batch files to generate the reports. These are generally not very interesting to other users as they are setup for my system. They are broken out into folders by number of desired targets.