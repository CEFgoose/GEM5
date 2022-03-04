        # for i in re.finditer(
        #     r"\*\s*(\[\s*osm_user_name\s*\(\s*\)|\[\s*setting\(\s*\"user_.*?\"\s*\)).*?}",  # noqa: E501
        #     mapcss_text,
        #     ):
        #     temp = i.group()
        #     print(temp)
        #     j = str(temp).split("}") 
        #     j = str(j).split("]")
        #     j= str(j).split("= ")
        #     j= str(j[1]).split('",')
        #     username = j[0]
        #     personname = re.findall(r"setting\(\s*\"user_(.*?)\"", temp)
        #     parsed_users[username] = {"name": personname[0]}





            # self.TEAMLINECOLORTEXT = re.findall(
    #     r"way:modified.*?casing-color:\s?([#0-9A-Za-z]*)", text_no_newline
    # )
    # self.TEAMLINECOLORTEXT = (
    #     self.TEAMLINECOLORTEXT[0]
    #     if isinstance(self.TEAMLINECOLORTEXT, list)
    #     else self.TEAMLINECOLORTEXT
    # )
    # self.TEAMNODECOLORTEXT = re.findall(
    #     r"node:modified.*?symbol-stroke-color:\s?([#0-9A-Za-z]*)", text_no_newline,
    # )
    # self.TEAMNODECOLORTEXT = (
    #     self.TEAMNODECOLORTEXT[0]
    #     if isinstance(self.TEAMNODECOLORTEXT, list)
    #     else self.TEAMNODECOLORTEXT
    # )
    # self.TEAMLINECOLORUI = QtGui.QColor(self.TEAMLINECOLORTEXT)
    # self.TEAMNODECOLORUI = QtGui.QColor(self.TEAMNODECOLORTEXT)
    # self.LINEWIDTH = re.findall(
    #     r"way:modified.*?casing-width\s?:\s?([0-9]+)", text_no_newline
    # )
    # self.LINEWIDTH = (
    #     self.LINEWIDTH[0] if isinstance(self.LINEWIDTH, list) else self.LINEWIDTH
    # )
    # self.ICONSIZE = re.findall(
    #     r"node:modified.*?symbol-size:\s?([0-9]+)", text_no_newline
    # )
    # self.ICONSIZE = (
    #     self.ICONSIZE[0] if isinstance(self.ICONSIZE, list) else self.ICONSIZE
    # )
    # self.TEAMICONSHAPE = re.findall(
    #     r"node:modified.*?symbol-shape:\s?([a-zA-Z]+)", text_no_newline
    # )
    # self.TEAMICONSHAPE = (
    #     self.TEAMICONSHAPE[0]
    #     if isinstance(self.TEAMICONSHAPE, list)
    #     else self.TEAMICONSHAPE
    # )

    # parsed_users = self.parse_line_colors_from_mapcss(text_no_newline, parsed_users)
    # parsed_users = self.parse_node_colors_from_mapcss(text_no_newline, parsed_users)
    # return parsed_users
