---
{
  "projection_kind": "taulib_declaration",
  "title": "e1_code_decode_structural",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-describing/e1-code-decode-structural/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.SelfDescribing`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfDescribing::e1_code_decode_structural",
  "declaration_slug": "e1-code-decode-structural",
  "kind": "theorem",
  "name": "e1_code_decode_structural",
  "module_name": "TauLib.BookII.Enrichment.SelfDescribing",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-describing/",
  "source_line_start": 261,
  "source_line_end": 264,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L261-L264",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.SelfDescribing",
        "url": "/verify/taulib/docs/book-ii-enrichment-self-describing/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L261-L264",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookII.Enrichment.SelfDescribing](/verify/taulib/docs/book-ii-enrichment-self-describing/)
- Source path: [`TauLib/BookII/Enrichment/SelfDescribing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L261-L264)
- Source range: L261-L264
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Code/Decode bijection correctness: Decode . Code = id for the identity.
    This is structural from code_decode_id_roundtrip in CodeDecode.lean. -/
```

## Source Excerpt

```lean
theorem e1_code_decode_structural (x k : TauIdx) :
    decode_reconstruct (fun a => code_extract (fun n => (n : Int)) k a) k x =
    code_extract (fun n => (n : Int)) k x :=
  code_decode_id_roundtrip x k
```
