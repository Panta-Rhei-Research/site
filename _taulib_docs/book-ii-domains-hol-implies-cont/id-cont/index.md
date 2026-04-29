---
{
  "projection_kind": "taulib_declaration",
  "title": "id_cont",
  "permalink": "/verify/taulib/docs/book-ii-domains-hol-implies-cont/id-cont/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Domains.HolImpliesCont`.",
  "declaration_id": "TauLib.BookII.Domains.HolImpliesCont::id_cont",
  "declaration_slug": "id-cont",
  "kind": "theorem",
  "name": "id_cont",
  "module_name": "TauLib.BookII.Domains.HolImpliesCont",
  "module_url": "/verify/taulib/docs/book-ii-domains-hol-implies-cont/",
  "source_line_start": 150,
  "source_line_end": 152,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/HolImpliesCont.lean#L150-L152",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Domains.HolImpliesCont",
        "url": "/verify/taulib/docs/book-ii-domains-hol-implies-cont/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/HolImpliesCont.lean#L150-L152",
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

- Module: [TauLib.BookII.Domains.HolImpliesCont](/verify/taulib/docs/book-ii-domains-hol-implies-cont/)
- Source path: [`TauLib/BookII/Domains/HolImpliesCont.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/HolImpliesCont.lean#L150-L152)
- Source range: L150-L152
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem id_cont : hol_cont_check id_stage 4 15 = true := by native_decide

end Tau.BookII.Domains
```
