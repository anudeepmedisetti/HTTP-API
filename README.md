# HTTP-API

The Source of this project is taken from "https://github.com/jdorfman/awesome-json-datasets#tv-shows" Which contain 14 popular shows.

# Our Goal:
1)We need to retrive the plain text from the source URL.
2)Understand the structute of the data.
3)Retrive the necessary variables from the unorganised data.
4)Develop a algorith to meed out final needs.

# Steps followed
1) Retrived one sample of the data and tried to vizualize the data using online vizualiser to better under stand the data.
which more looked like this:
{
  "id": 1871,
  "url": "http://www.tvmaze.com/shows/1871/mr-robot",
  "name": "Mr. Robot",
  "type": "Scripted",
  "language": "English",
  "genres": [
    "Drama",
    "Crime",
    "Thriller"
  ],
  "status": "Ended",
  "runtime": 60,
  "premiered": "2015-06-24",
  "officialSite": "http://www.usanetwork.com/mrrobot",
  "schedule": {
    "time": "22:00",
    "days": [
      "Sunday"
    ]
  },
  "rating": {
    "average": 8.4
  },
  "weight": 93,
  "network": {
    "id": 30,
    "name": "USA Network",
    "country": {
      "name": "United States",
      "code": "US",
      "timezone": "America/New_York"
    }
  },
  "webChannel": null,
  "externals": {
    "tvrage": 42422,
    "thetvdb": 289590,
    "imdb": "tt4158110"
  },
  "image": {
    "medium": "http://static.tvmaze.com/uploads/images/medium_portrait/211/528026.jpg",
    "original": "http://static.tvmaze.com/uploads/images/original_untouched/211/528026.jpg"
  },
  "summary": "<p><b>Mr. Robot</b> follows Elliot, a young programmer who works as a cyber-security engineer by day and as a vigilante hacker by night. Elliot finds himself at a crossroads when the mysterious leader of an underground hacker group recruits him to destroy the firm he is paid to protect. Compelled by his personal beliefs, Elliot struggles to resist the chance to take down the multinational CEOs he believes are running (and ruining) the world.</p>",
  "updated": 1579127077,
  "_links": {
    "self": {
      "href": "http://api.tvmaze.com/shows/1871"
    },
    "previousepisode": {
      "href": "http://api.tvmaze.com/episodes/1762042"
    }
  },
  "_embedded": {
    "episodes": [
      {
        "id": 157154,
        "url": "http://www.tvmaze.com/episodes/157154/mr-robot-1x01-eps10hellofriendmov",
        "name": "eps1.0_hellofriend.mov",
        "season": 1,
        "number": 1,
        "type": "regular",
        "airdate": "2015-06-24",
        "airtime": "22:00",
        "airstamp": "2015-06-25T02:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/106/266370.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/106/266370.jpg"
        },
        "summary": "<p>In MR. ROBOT, Elliot, a cyber-security engineer by day and vigilante hacker by night, is recruited by a mysterious underground group to destroy the firm he's paid to protect. Elliot must decide how far he'll go to expose the forces he believes are running (and ruining) the world.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/157154"
          }
        }
      },
      {
        "id": 167379,
        "url": "http://www.tvmaze.com/episodes/167379/mr-robot-1x02-eps11ones-and-zer0esmpeg",
        "name": "eps1.1_ones-and-zer0es.mpeg",
        "season": 1,
        "number": 2,
        "type": "regular",
        "airdate": "2015-07-01",
        "airtime": "22:00",
        "airstamp": "2015-07-02T02:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/12/31833.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/12/31833.jpg"
        },
        "summary": "<p>Tyrell Wellick, now Evil Corp's acting CTO since Elliot helped get Terry Colby arrested, makes Elliot an offer he can (and does) refuse: a position as Evil Corp's head of Cyber Security and a big bank account to match. By saying no, has Elliot made himself a mark for Wellick?</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/167379"
          }
        }
      },
      {
        "id": 167380,
        "url": "http://www.tvmaze.com/episodes/167380/mr-robot-1x03-eps12d3bugmkv",
        "name": "eps1.2_d3bug.mkv",
        "season": 1,
        "number": 3,
        "type": "regular",
        "airdate": "2015-07-08",
        "airtime": "22:00",
        "airstamp": "2015-07-09T02:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/106/266701.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/106/266701.jpg"
        },
        "summary": "<p>After being shoved off the railing in Coney Island by Mr. Robot, Elliot wakes up in a hospital room, badly banged up. Krista, his psychiatrist, is inclined to send him to rehab unless he's willing to be regularly drug tested. Elliot complies, knowing that he can easily change the hospital records for the tests since he hacked their system long ago.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/167380"
          }
        }
      },
      {
        "id": 167381,
        "url": "http://www.tvmaze.com/episodes/167381/mr-robot-1x04-eps13da3m0nsmp4",
        "name": "eps1.3_da3m0ns.mp4",
        "season": 1,
        "number": 4,
        "type": "regular",
        "airdate": "2015-07-15",
        "airtime": "22:00",
        "airstamp": "2015-07-16T02:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/106/267080.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/106/267080.jpg"
        },
        "summary": "<p>At fsociety, Elliot lays out his plan to hack Steel Mountain's climate control system and raise the heat high enough to melt all the tapes that record the data. Romero points out the plan's many flaws but when Elliot remembers that they only have a few days left before Evil Corp switches over to their new redundant security protocols based on what Tyrell Wellick told him, they reluctantly agree it's now or never.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/167381"
          }
        }
      },
      {
        "id": 167382,
        "url": "http://www.tvmaze.com/episodes/167382/mr-robot-1x05-eps143xpl0itswmv",
        "name": "eps1.4_3xpl0its.wmv",
        "season": 1,
        "number": 5,
        "type": "regular",
        "airdate": "2015-07-22",
        "airtime": "22:00",
        "airstamp": "2015-07-23T02:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/106/267095.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/106/267095.jpg"
        },
        "summary": "<p>Fsociety attempts to penetrate Steel Mountain, the most secure data facility in America.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/167382"
          }
        }
      },
      {
        "id": 167383,
        "url": "http://www.tvmaze.com/episodes/167383/mr-robot-1x06-eps15br4ve-trave1erasf",
        "name": "eps1.5_br4ve-trave1er.asf",
        "season": 1,
        "number": 6,
        "type": "regular",
        "airdate": "2015-07-29",
        "airtime": "22:00",
        "airstamp": "2015-07-30T02:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/106/267138.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/106/267138.jpg"
        },
        "summary": "<p>Elliot attempts to hack Vera out of jail in order to save someone he cares about; Tyrell's \"game\" gets crazy; and Angela digs deeper into her mother's death.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/167383"
          }
        }
      },
      {
        "id": 167384,
        "url": "http://www.tvmaze.com/episodes/167384/mr-robot-1x07-eps16v1ew-s0urceflv",
        "name": "eps1.6_v1ew-s0urce.flv",
        "season": 1,
        "number": 7,
        "type": "regular",
        "airdate": "2015-08-05",
        "airtime": "22:00",
        "airstamp": "2015-08-06T02:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/14/35974.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/14/35974.jpg"
        },
        "summary": "<p>Elliott goes missing; Mr. Robot tries to pull fsociety back together; Angela goes head-to-head with an old nemesis.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/167384"
          }
        }
      },
      {
        "id": 167385,
        "url": "http://www.tvmaze.com/episodes/167385/mr-robot-1x08-eps17wh1ter0sem4v",
        "name": "eps1.7_wh1ter0se.m4v",
        "season": 1,
        "number": 8,
        "type": "regular",
        "airdate": "2015-08-12",
        "airtime": "21:00",
        "airstamp": "2015-08-13T01:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/106/267485.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/106/267485.jpg"
        },
        "summary": "<p>Allsafe is controlled; the Dark Army is ready to meet Elliot; and Tyrell and Joanna's plan goes into effect.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/167385"
          }
        }
      },
      {
        "id": 167386,
        "url": "http://www.tvmaze.com/episodes/167386/mr-robot-1x09-eps18m1rr0r1ngqt",
        "name": "eps1.8_m1rr0r1ng.qt",
        "season": 1,
        "number": 9,
        "type": "regular",
        "airdate": "2015-08-19",
        "airtime": "21:00",
        "airstamp": "2015-08-20T01:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/107/267502.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/107/267502.jpg"
        },
        "summary": "<p>The Evil Corp hack is threatened by a mystery man from Elliot's past.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/167386"
          }
        }
      },
      {
        "id": 167387,
        "url": "http://www.tvmaze.com/episodes/167387/mr-robot-1x10-eps19zer0-dayavi",
        "name": "eps1.9_zer0-day.avi",
        "season": 1,
        "number": 10,
        "type": "regular",
        "airdate": "2015-09-02",
        "airtime": "22:00",
        "airstamp": "2015-09-03T02:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/107/267554.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/107/267554.jpg"
        },
        "summary": "<p>In the Season 1 finale, Mr. Robot and Tyrell are MIA; and a past hack haunts Elliot.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/167387"
          }
        }
      },
      {
        "id": 733139,
        "url": "http://www.tvmaze.com/episodes/733139/mr-robot-2x01-eps20unm4sk-pt1tc",
        "name": "eps2.0_unm4sk-pt1.tc",
        "season": 2,
        "number": 1,
        "type": "regular",
        "airdate": "2016-07-13",
        "airtime": "22:00",
        "airstamp": "2016-07-14T02:00:00+00:00",
        "runtime": 46,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/67/168565.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/67/168565.jpg"
        },
        "summary": "<p>one month later and omfg, five/nine changed the world. elliot in seclusion. darlene takes the lead. fsociety delivers malicious payload. TANGO DOWN? tbc.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/733139"
          }
        }
      },
      {
        "id": 830870,
        "url": "http://www.tvmaze.com/episodes/830870/mr-robot-2x02-eps20unm4sk-pt2tc",
        "name": "eps2.0_unm4sk-pt2.tc",
        "season": 2,
        "number": 2,
        "type": "regular",
        "airdate": "2016-07-13",
        "airtime": "22:46",
        "airstamp": "2016-07-14T02:46:00+00:00",
        "runtime": 46,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/67/168564.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/67/168564.jpg"
        },
        "summary": "<p>angela happy at evil corp. tyrell MIA and joanna has a new bf? wtf? dom leads fbi investigation into five/nine. elliot demands answers from mr. robot.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/830870"
          }
        }
      },
      {
        "id": 830871,
        "url": "http://www.tvmaze.com/episodes/830871/mr-robot-2x03-eps21k3rnel-pan1cksd",
        "name": "eps2.1_k3rnel-pan1c.ksd",
        "season": 2,
        "number": 3,
        "type": "regular",
        "airdate": "2016-07-20",
        "airtime": "22:00",
        "airstamp": "2016-07-21T02:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/107/268499.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/107/268499.jpg"
        },
        "summary": "<p>Elliot vows to beat Mr. Robot but it ain't easy, smh. Angela sees behind the scenes at Evil Corp. Sh*t hits fan with fsociety.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/830871"
          }
        }
      },
      {
        "id": 830872,
        "url": "http://www.tvmaze.com/episodes/830872/mr-robot-2x04-eps22init1asec",
        "name": "eps2.2_init1.asec",
        "season": 2,
        "number": 4,
        "type": "regular",
        "airdate": "2016-07-27",
        "airtime": "22:00",
        "airstamp": "2016-07-28T02:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/107/268493.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/107/268493.jpg"
        },
        "summary": "<p>Elliot friends Ray, who he hopes can help delete Mr. Robot; Dom makes a major discovery; and Darlene questions whether the FBI or Dark Army is the bigger threat.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/830872"
          }
        }
      },
      {
        "id": 830873,
        "url": "http://www.tvmaze.com/episodes/830873/mr-robot-2x05-eps23logic-b0mbhc",
        "name": "eps2.3_logic-b0mb.hc",
        "season": 2,
        "number": 5,
        "type": "regular",
        "airdate": "2016-08-03",
        "airtime": "22:01",
        "airstamp": "2016-08-04T02:01:00+00:00",
        "runtime": 72,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/107/268475.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/107/268475.jpg"
        },
        "summary": "<p>Elliot can't quit the game; Dom and the FBI head to China to investigate 5/9; Joanna is haunted; and Darlene calls on Angela for help.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/830873"
          }
        }
      },
      {
        "id": 830874,
        "url": "http://www.tvmaze.com/episodes/830874/mr-robot-2x06-eps24m4ster-s1aveaes",
        "name": "eps2.4_m4ster-s1ave.aes",
        "season": 2,
        "number": 6,
        "type": "regular",
        "airdate": "2016-08-10",
        "airtime": "22:01",
        "airstamp": "2016-08-11T02:01:00+00:00",
        "runtime": 70,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/70/176488.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/70/176488.jpg"
        },
        "summary": "<p>Mr. Robot tries to show Elliot that he can be useful; and Darlene and Angela's plan doesn't go as hoped.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/830874"
          }
        }
      },
      {
        "id": 830875,
        "url": "http://www.tvmaze.com/episodes/830875/mr-robot-2x07-eps25h4ndshakesme",
        "name": "eps2.5_h4ndshake.sme",
        "season": 2,
        "number": 7,
        "type": "regular",
        "airdate": "2016-08-17",
        "airtime": "22:01",
        "airstamp": "2016-08-18T02:01:00+00:00",
        "runtime": 70,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/71/178952.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/71/178952.jpg"
        },
        "summary": "<p>Mr. Robot and Elliot try to make nice; and Joanna is given an ultimatum.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/830875"
          }
        }
      },
      {
        "id": 830876,
        "url": "http://www.tvmaze.com/episodes/830876/mr-robot-2x08-eps26succ3ss0rp12",
        "name": "eps2.6_succ3ss0r.p12",
        "season": 2,
        "number": 8,
        "type": "regular",
        "airdate": "2016-08-24",
        "airtime": "22:00",
        "airstamp": "2016-08-25T02:00:00+00:00",
        "runtime": 67,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/107/268442.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/107/268442.jpg"
        },
        "summary": "<p>A video is released by fsociety; Darlene decides to act on an old desire.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/830876"
          }
        }
      },
      {
        "id": 830877,
        "url": "http://www.tvmaze.com/episodes/830877/mr-robot-2x09-eps27init5fve",
        "name": "eps2.7_init5.fve",
        "season": 2,
        "number": 9,
        "type": "regular",
        "airdate": "2016-08-31",
        "airtime": "22:00",
        "airstamp": "2016-09-01T02:00:00+00:00",
        "runtime": 65,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/73/182686.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/73/182686.jpg"
        },
        "summary": "<p>Angela wants more from E Corp than they want to give; and Elliot and Darlene seek answers.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/830877"
          }
        }
      },
      {
        "id": 830878,
        "url": "http://www.tvmaze.com/episodes/830878/mr-robot-2x10-eps28h1dden-pr0cessaxx",
        "name": "eps2.8_h1dden-pr0cess.axx",
        "season": 2,
        "number": 10,
        "type": "regular",
        "airdate": "2016-09-07",
        "airtime": "22:00",
        "airstamp": "2016-09-08T02:00:00+00:00",
        "runtime": 65,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/73/184601.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/73/184601.jpg"
        },
        "summary": "<p>Elliot wonders if Mr. Robot has been lying to him; Darlene attempts to do the right thing; Dom and the FBI get closer.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/830878"
          }
        }
      },
      {
        "id": 861461,
        "url": "http://www.tvmaze.com/episodes/861461/mr-robot-2x11-eps29pyth0n-pt1p7z",
        "name": "eps2.9_pyth0n-pt1.p7z",
        "season": 2,
        "number": 11,
        "type": "regular",
        "airdate": "2016-09-14",
        "airtime": "22:00",
        "airstamp": "2016-09-15T02:00:00+00:00",
        "runtime": 70,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/107/268408.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/107/268408.jpg"
        },
        "summary": "<p>Angela makes an unexpected acquaintance. Elliot does the same. Dom engages in an interesting ama.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/861461"
          }
        }
      },
      {
        "id": 910146,
        "url": "http://www.tvmaze.com/episodes/910146/mr-robot-2x12-eps29pyth0n-pt2p7z",
        "name": "eps2.9_pyth0n-pt2.p7z",
        "season": 2,
        "number": 12,
        "type": "regular",
        "airdate": "2016-09-21",
        "airtime": "22:00",
        "airstamp": "2016-09-22T02:00:00+00:00",
        "runtime": 66,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/76/190198.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/76/190198.jpg"
        },
        "summary": "<p>Darlene realizes she is in too deep; an old friend reveals everything to Elliot.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/910146"
          }
        }
      },
      {
        "id": 1184709,
        "url": "http://www.tvmaze.com/episodes/1184709/mr-robot-3x01-eps30power-saver-modeh",
        "name": "eps3.0_power-saver-mode.h",
        "season": 3,
        "number": 1,
        "type": "regular",
        "airdate": "2017-10-11",
        "airtime": "22:00",
        "airstamp": "2017-10-12T02:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/130/327445.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/130/327445.jpg"
        },
        "summary": "<p>Elliot realizes his mission, and needs help from Angela; Darlene worries about them coming out clean.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1184709"
          }
        }
      },
      {
        "id": 1215786,
        "url": "http://www.tvmaze.com/episodes/1215786/mr-robot-3x02-eps31undogz",
        "name": "eps3.1_undo.gz",
        "season": 3,
        "number": 2,
        "type": "regular",
        "airdate": "2017-10-18",
        "airtime": "22:00",
        "airstamp": "2017-10-19T02:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/131/329581.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/131/329581.jpg"
        },
        "summary": "<p>Elliot becomes encouraged trying to undo five/nine; Darlene gets stuck between a rock and a hard place; Mr. Robot sparks a panic.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1215786"
          }
        }
      },
      {
        "id": 1215788,
        "url": "http://www.tvmaze.com/episodes/1215788/mr-robot-3x03-eps32legacyso",
        "name": "eps3.2_legacy.so",
        "season": 3,
        "number": 3,
        "type": "regular",
        "airdate": "2017-10-25",
        "airtime": "22:00",
        "airstamp": "2017-10-26T02:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/132/331608.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/132/331608.jpg"
        },
        "summary": "<p>The former interim CTO of E Corp returns.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1215788"
          }
        }
      },
      {
        "id": 1215789,
        "url": "http://www.tvmaze.com/episodes/1215789/mr-robot-3x04-eps33metadatapar2",
        "name": "eps3.3_metadata.par2",
        "season": 3,
        "number": 4,
        "type": "regular",
        "airdate": "2017-11-01",
        "airtime": "22:00",
        "airstamp": "2017-11-02T02:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/133/334012.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/133/334012.jpg"
        },
        "summary": "<p>Dom has a close call; Elliot chases himself with Darlene on the lookout.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1215789"
          }
        }
      },
      {
        "id": 1215790,
        "url": "http://www.tvmaze.com/episodes/1215790/mr-robot-3x05-eps34runtime-err0rr00",
        "name": "eps3.4_runtime-err0r.r00",
        "season": 3,
        "number": 5,
        "type": "regular",
        "airdate": "2017-11-08",
        "airtime": "22:00",
        "airstamp": "2017-11-09T03:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/134/335889.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/134/335889.jpg"
        },
        "summary": "<p>E Corp is in chaos; Elliot is on the run; Darlene tries to help.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1215790"
          }
        }
      },
      {
        "id": 1215791,
        "url": "http://www.tvmaze.com/episodes/1215791/mr-robot-3x06-eps35kill-pr0cessinc",
        "name": "eps3.5_kill-pr0cess.inc",
        "season": 3,
        "number": 6,
        "type": "regular",
        "airdate": "2017-11-15",
        "airtime": "22:00",
        "airstamp": "2017-11-16T03:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/135/338259.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/135/338259.jpg"
        },
        "summary": "<p>Elliot faces off with Mr. Robot; Dom gets tired of the red tape; Tyrell has a new plan.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1215791"
          }
        }
      },
      {
        "id": 1215794,
        "url": "http://www.tvmaze.com/episodes/1215794/mr-robot-3x07-eps36fredricktanyachk",
        "name": "eps3.6_fredrick+tanya.chk",
        "season": 3,
        "number": 7,
        "type": "regular",
        "airdate": "2017-11-22",
        "airtime": "22:00",
        "airstamp": "2017-11-23T03:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/136/340402.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/136/340402.jpg"
        },
        "summary": "<p>Mr. Robot wants answers; the FBI closes in; Angela hits the rewind button.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1215794"
          }
        }
      },
      {
        "id": 1215795,
        "url": "http://www.tvmaze.com/episodes/1215795/mr-robot-3x08-eps37dont-delete-meko",
        "name": "eps3.7_dont-delete-me.ko",
        "season": 3,
        "number": 8,
        "type": "regular",
        "airdate": "2017-11-29",
        "airtime": "22:00",
        "airstamp": "2017-11-30T03:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/136/342249.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/136/342249.jpg"
        },
        "summary": "<p>Elliot tries to get ghosted; it is the day of all days.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1215795"
          }
        }
      },
      {
        "id": 1215796,
        "url": "http://www.tvmaze.com/episodes/1215796/mr-robot-3x09-eps38stage3torrent",
        "name": "eps3.8_stage3.torrent",
        "season": 3,
        "number": 9,
        "type": "regular",
        "airdate": "2017-12-06",
        "airtime": "22:00",
        "airstamp": "2017-12-07T03:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/137/344253.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/137/344253.jpg"
        },
        "summary": "<p>Elliot trolls a former ally; Mr. Robot leaves cryptic text; Tyrell gets new commands.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1215796"
          }
        }
      },
      {
        "id": 1215797,
        "url": "http://www.tvmaze.com/episodes/1215797/mr-robot-3x10-shutdown-r",
        "name": "shutdown -r",
        "season": 3,
        "number": 10,
        "type": "regular",
        "airdate": "2017-12-13",
        "airtime": "22:00",
        "airstamp": "2017-12-14T03:00:00+00:00",
        "runtime": 75,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/138/346172.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/138/346172.jpg"
        },
        "summary": "<p>Elliot tries to save Darlene but things don't go as planned. Mr. Robot must decide whether to step up or step back. Angela considers the price.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1215797"
          }
        }
      },
      {
        "id": 1705714,
        "url": "http://www.tvmaze.com/episodes/1705714/mr-robot-4x01-401-unauthorized",
        "name": "401 Unauthorized",
        "season": 4,
        "number": 1,
        "type": "regular",
        "airdate": "2019-10-06",
        "airtime": "22:00",
        "airstamp": "2019-10-07T02:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/214/536060.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/214/536060.jpg"
        },
        "summary": "<p>During the Christmas season, Elliot and Mr. Robot make their return; Darlene deals with real trouble; Tyrell is bored; Dom becomes paranoid.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1705714"
          }
        }
      },
      {
        "id": 1723152,
        "url": "http://www.tvmaze.com/episodes/1723152/mr-robot-4x02-402-payment-required",
        "name": "402 Payment Required",
        "season": 4,
        "number": 2,
        "type": "regular",
        "airdate": "2019-10-13",
        "airtime": "22:00",
        "airstamp": "2019-10-14T02:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/215/538745.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/215/538745.jpg"
        },
        "summary": "<p>Elliot and Darlene come together. Dom gets dark army vibes. Price has answers.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1723152"
          }
        }
      },
      {
        "id": 1728848,
        "url": "http://www.tvmaze.com/episodes/1728848/mr-robot-4x03-403-forbidden",
        "name": "403 Forbidden",
        "season": 4,
        "number": 3,
        "type": "regular",
        "airdate": "2019-10-20",
        "airtime": "22:00",
        "airstamp": "2019-10-21T02:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/216/541937.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/216/541937.jpg"
        },
        "summary": "<p>Whiterose has the feels. Elliot gets owned by his own hack. An old foe waits.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1728848"
          }
        }
      },
      {
        "id": 1733128,
        "url": "http://www.tvmaze.com/episodes/1733128/mr-robot-4x04-404-not-found",
        "name": "404 Not Found",
        "season": 4,
        "number": 4,
        "type": "regular",
        "airdate": "2019-10-27",
        "airtime": "22:00",
        "airstamp": "2019-10-28T02:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/217/544375.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/217/544375.jpg"
        },
        "summary": "<p>Tyrell, Elliot, and Mr. Robot go on a perilous journey through the woods; Darlene deals with her feelings when she has to take a drunk Santa home; Dom is aroused and has a nightmare.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1733128"
          }
        }
      },
      {
        "id": 1742746,
        "url": "http://www.tvmaze.com/episodes/1742746/mr-robot-4x05-405-method-not-allowed",
        "name": "405 Method Not Allowed",
        "season": 4,
        "number": 5,
        "type": "regular",
        "airdate": "2019-11-03",
        "airtime": "22:00",
        "airstamp": "2019-11-04T03:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/218/545690.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/218/545690.jpg"
        },
        "summary": "<p>Dom has no fun on Chrismas; Darlene and Elliot give a run-around; Krista plays hooky.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1742746"
          }
        }
      },
      {
        "id": 1746057,
        "url": "http://www.tvmaze.com/episodes/1746057/mr-robot-4x06-406-not-acceptable",
        "name": "406 Not Acceptable",
        "season": 4,
        "number": 6,
        "type": "regular",
        "airdate": "2019-11-10",
        "airtime": "20:00",
        "airstamp": "2019-11-11T01:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/221/553091.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/221/553091.jpg"
        },
        "summary": "<p>Vera tells a tale. Darlene gets a Christmas surprise. Elliot goes rogue.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1746057"
          }
        }
      },
      {
        "id": 1752609,
        "url": "http://www.tvmaze.com/episodes/1752609/mr-robot-4x07-407-proxy-authentication-required",
        "name": "407 Proxy Authentication Required",
        "season": 4,
        "number": 7,
        "type": "regular",
        "airdate": "2019-11-17",
        "airtime": "22:00",
        "airstamp": "2019-11-18T03:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/224/561942.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/224/561942.jpg"
        },
        "summary": "<p>Vera holds Krista hostage as he tries to force Elliott into joining him by understanding Mr. Robot. Elliot realizes a shocking truth.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1752609"
          }
        }
      },
      {
        "id": 1754672,
        "url": "http://www.tvmaze.com/episodes/1754672/mr-robot-4x08-408-request-timeout",
        "name": "408 Request Timeout",
        "season": 4,
        "number": 8,
        "type": "regular",
        "airdate": "2019-11-24",
        "airtime": "22:00",
        "airstamp": "2019-11-25T03:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/227/568779.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/227/568779.jpg"
        },
        "summary": "<p>Janice tries to get Elliot's location from Dom and Darlene. Elliot goes to the Queens Museum.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1754672"
          }
        }
      },
      {
        "id": 1759731,
        "url": "http://www.tvmaze.com/episodes/1759731/mr-robot-4x09-409-conflict",
        "name": "409 Conflict",
        "season": 4,
        "number": 9,
        "type": "regular",
        "airdate": "2019-12-01",
        "airtime": "22:00",
        "airstamp": "2019-12-02T03:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/228/571952.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/228/571952.jpg"
        },
        "summary": "<p>fsociety v deus group. Fsociety faces off against Deus Group.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1759731"
          }
        }
      },
      {
        "id": 1762039,
        "url": "http://www.tvmaze.com/episodes/1762039/mr-robot-4x10-410-gone",
        "name": "410 Gone",
        "season": 4,
        "number": 10,
        "type": "regular",
        "airdate": "2019-12-08",
        "airtime": "22:00",
        "airstamp": "2019-12-09T03:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/230/575698.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/230/575698.jpg"
        },
        "summary": "<p>we stan domlene. Fans like Dom and Darlene.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1762039"
          }
        }
      },
      {
        "id": 1762040,
        "url": "http://www.tvmaze.com/episodes/1762040/mr-robot-4x11-exit",
        "name": "eXit",
        "season": 4,
        "number": 11,
        "type": "regular",
        "airdate": "2019-12-15",
        "airtime": "22:00",
        "airstamp": "2019-12-16T03:00:00+00:00",
        "runtime": 60,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/231/579176.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/231/579176.jpg"
        },
        "summary": "<p>Enough is enough. Elliot goes to the Washington Township power plant.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1762040"
          }
        }
      },
      {
        "id": 1762041,
        "url": "http://www.tvmaze.com/episodes/1762041/mr-robot-4x12-whoami",
        "name": "whoami",
        "season": 4,
        "number": 12,
        "type": "regular",
        "airdate": "2019-12-22",
        "airtime": "21:00",
        "airstamp": "2019-12-23T02:00:00+00:00",
        "runtime": 61,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/232/581610.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/232/581610.jpg"
        },
        "summary": "<p>Nothing is as it appears in our new world.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1762041"
          }
        }
      },
      {
        "id": 1762042,
        "url": "http://www.tvmaze.com/episodes/1762042/mr-robot-4x13-hello-elliot",
        "name": "Hello, Elliot",
        "season": 4,
        "number": 13,
        "type": "regular",
        "airdate": "2019-12-22",
        "airtime": "22:00",
        "airstamp": "2019-12-23T03:00:00+00:00",
        "runtime": 66,
        "image": {
          "medium": "http://static.tvmaze.com/uploads/images/medium_landscape/232/581609.jpg",
          "original": "http://static.tvmaze.com/uploads/images/original_untouched/232/581609.jpg"
        },
        "summary": "<p>It's finally time to learn the truth, friend.</p>",
        "_links": {
          "self": {
            "href": "http://api.tvmaze.com/episodes/1762042"
          }
        }
      }
    ]
  }
}


2)Then I compared the data of this sample to other samples and found all have the similar structure.
3)Started to work on one sample of data(studing and going through it).
4)Firstly, I have converted the data from JSon to plain text.
5)The above Json vizualiser had given we an idea of which variables to be isolated.
6)secondly, I isolated the necessary variable and stored in a data frame.
7)finally , I have used the dataframe to develop an algorith to meet our needs.


# Approximate Run-time of developed algorithm:

Runtime = O(1)+ 2(O(n))+(O(n^2))
