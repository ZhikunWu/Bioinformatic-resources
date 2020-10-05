#!/usr/bin/env python
import sqlite3
import argparse

#usage: python ~/github/zkwu/kcMeta/src/kcMeta/taxonomy2DB.py --node /home/wzk/database/taxonomy/nodes.dmp --name /home/wzk/database/taxonomy/names.dmp --database /home/wzk/database/taxonomy/taxanomy-1.db

__author__ = "Zhikun Wu"
__date__  = "2018.10.09"
__email__ = "598466208@qq.com"

def parse_names_dmp(name_dmp):
    IdName = {}
    name_h = open(name_dmp, "r")
    for line in name_h:
        if "scientific name" in line:
            lines = line.strip().split("\t")
            taxa_id = lines[0]
            taxa_id = int(taxa_id)
            taxa_name = lines[2]
            IdName[taxa_id] = taxa_name
    name_h.close()
    return IdName

def parse_nodes_dmp(name_dmp, node_dmp, out_db):
    conn = sqlite3.connect(out_db)
    cursor = conn.cursor()
    ### create the table containing descendant id and parent id
    cursor.execute("""
        CREATE TABLE TaxaParent 
        (taxa_id integer,
        parent_id integer);
    """)
    ### create the table containing taxa id, taxa name and level
    cursor.execute("""
        CREATE TABLE TaxaNameLevel
        (taxa_id integer,
        taxa_name text,
        taxa_level text);
    """)
    ### get the dict if taxa id and taxa name
    IdName = parse_names_dmp(name_dmp)
    node_h = open(node_dmp, "r")
    for line in node_h:
        lines = line.strip().split("\t")
        taxa_id = lines[0]
        taxa_id = int(taxa_id)
        parent_id = lines[2]
        parent_id = int(parent_id)
        cursor.execute("""
            INSERT INTO TaxaParent
            (taxa_id, parent_id)
            VALUES
            (?, ?);
        """, (taxa_id, parent_id))
        level = lines[4]
        if taxa_id in IdName:
            taxa_name = IdName[taxa_id]
            cursor.execute("""
                INSERT INTO TaxaNameLevel
                (taxa_id,
                taxa_name,
                taxa_level)
                VALUES
                (?, ?, ?);
            """, (taxa_id, taxa_name, level))
    node_h.close()
    ### create index for table
    cursor.execute("""
        CREATE INDEX 
        taxaId on TaxaParent (taxa_id);
    """)
    cursor.execute("""
        CREATE INDEX 
        TaId on TaxaNameLevel (taxa_id);
    """)
    cursor.close()
    conn.commit()
    conn.close()

def main():
    parser = argparse.ArgumentParser(description="Get the database for taxonomy nodes and names.")
    parser.add_argument("-e", "--node", help="The input node file of NCBI taxonomy.")
    parser.add_argument("-n", "--name", help="The input name file of NCBI taxonomy.")
    parser.add_argument("-d", "--database", help="The output database.")
    args = parser.parse_args()
    parse_nodes_dmp(args.name, args.node, args.database)

if __name__ == "__main__":
    main()
    

