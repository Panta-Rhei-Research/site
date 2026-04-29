---
{
  "projection_kind": "taulib_declaration",
  "title": "tau3_round_trip'",
  "permalink": "/verify/taulib/docs/book-ii-interior-tau3-fibration/tau3-round-trip-l101/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Interior.Tau3Fibration`.",
  "declaration_id": "TauLib.BookII.Interior.Tau3Fibration::tau3_round_trip'",
  "declaration_slug": "tau3-round-trip-l101",
  "kind": "theorem",
  "name": "tau3_round_trip'",
  "module_name": "TauLib.BookII.Interior.Tau3Fibration",
  "module_url": "/verify/taulib/docs/book-ii-interior-tau3-fibration/",
  "source_line_start": 101,
  "source_line_end": 103,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L101-L103",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.Tau3Fibration",
        "url": "/verify/taulib/docs/book-ii-interior-tau3-fibration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L101-L103",
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

- Module: [TauLib.BookII.Interior.Tau3Fibration](/verify/taulib/docs/book-ii-interior-tau3-fibration/)
- Source path: [`TauLib/BookII/Interior/Tau3Fibration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L101-L103)
- Source range: L101-L103
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- to_tau3 ∘ from_tau3 = id. -/
```

## Source Excerpt

```lean
theorem tau3_round_trip' (t : Tau3) :
    to_tau3 (from_tau3 t) = t := by
  simp [to_tau3, from_tau3]
```
