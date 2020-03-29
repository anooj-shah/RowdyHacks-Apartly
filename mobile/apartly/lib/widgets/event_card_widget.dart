import 'package:animated_card/animated_card.dart';
import 'package:apartly/utilities/constants.dart';
import 'package:badges/badges.dart';
import 'package:circular_check_box/circular_check_box.dart';
import 'package:flutter/material.dart';

class EventCard extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Padding(
        padding: const EdgeInsets.all(0.0),
        child: AnimatedCard(
          direction: AnimatedCardDirection.left,
          //Initial animation direction
          initDelay: Duration(milliseconds: 0),
          //Delay to initial animation
          duration: Duration(seconds: 1),
          //Initial animation duration
//        onRemove: () => lista.removeAt(index), //Implement this action to active dismiss
          curve: Curves.easeInOutSine,
          //Animation curve
          child: Container(
            height: 300,
//          color: Constants.theme,
            padding: EdgeInsets.symmetric(horizontal: 10),
            child: Card(
//            color: Constants.themePurple,
              elevation: 5,
              child: ListTile(
                title: Stack(children: [

                  Column(
                    children: [
                      Padding(
                        padding: const EdgeInsets.all(14.0),
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: <Widget>[
                            Text("Title"),
                            Padding(
                              padding: const EdgeInsets.all(8.0),
                              child: Badge(
                                badgeColor: Constants.themePurple,
                                padding: const EdgeInsets.all(10.0),
                                shape: BadgeShape.square,
                                borderRadius: 8,
                                toAnimate: false,
                                badgeContent: Text('10:30AM',
                                    style: TextStyle(color: Colors.white)),
                              ),
                            ),
                          ],
                        ),
                      ),
                      Container(
//constraints: BoxConstraints.tight(Size(100,150)),
                        height: 150,
                        width: 150,
                        child: ClipOval(
                          child: Image.asset("assets/dice.gif"),
                        ), //Center(child: Text("3534534")),
                      ),
                      Row(
                        children: <Widget>[
                          Padding(
                            padding: const EdgeInsets.all(8.0),
                            child: Badge(
                              badgeColor: Colors.deepPurple,
                              padding: const EdgeInsets.all(10.0),
                              shape: BadgeShape.square,
                              borderRadius: 8,
                              toAnimate: false,
                              badgeContent: Text('Fun',
                                  style: TextStyle(color: Colors.white)),
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.all(8.0),
                            child: Badge(
                              badgeColor: Colors.deepPurple,
                              shape: BadgeShape.square,
                              padding: const EdgeInsets.all(10.0),
                              borderRadius: 8,
                              toAnimate: false,
                              badgeContent: Text('Learning',
                                  style: TextStyle(color: Colors.white)),
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.all(8.0),
                            child: Badge(
                              badgeColor: Colors.deepPurple,
                              shape: BadgeShape.square,
                              padding: const EdgeInsets.all(10.0),
                              borderRadius: 8,
                              toAnimate: false,
                              badgeContent: Text('Games',
                                  style: TextStyle(color: Colors.white)),
                            ),
                          ),
                        ],
                      )
                    ],
                  ),
                  Positioned(
                      right: 0,
                      child: CircularCheckBox(
                          value: true,
                          materialTapTargetSize: MaterialTapTargetSize.padded,
                          onChanged: (bool x) {
//                            someBooleanValue = !someBooleanValue;
                          }
                      )),
                ]),
              ),
            ),
          ),
        ));
  }
}
