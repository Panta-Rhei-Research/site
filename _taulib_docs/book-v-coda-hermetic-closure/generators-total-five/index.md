---
{
  "projection_kind": "taulib_declaration",
  "title": "generators_total_five",
  "permalink": "/verify/taulib/docs/book-v-coda-hermetic-closure/generators-total-five/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Coda.HermeticClosure`.",
  "declaration_id": "TauLib.BookV.Coda.HermeticClosure::generators_total_five",
  "declaration_slug": "generators-total-five",
  "kind": "theorem",
  "name": "generators_total_five",
  "module_name": "TauLib.BookV.Coda.HermeticClosure",
  "module_url": "/verify/taulib/docs/book-v-coda-hermetic-closure/",
  "source_line_start": 109,
  "source_line_end": 110,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L109-L110",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.HermeticClosure",
        "url": "/verify/taulib/docs/book-v-coda-hermetic-closure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L109-L110",
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

- Module: [TauLib.BookV.Coda.HermeticClosure](/verify/taulib/docs/book-v-coda-hermetic-closure/)
- Source path: [`TauLib/BookV/Coda/HermeticClosure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L109-L110)
- Source range: L109-L110
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Base + fiber generators sum to 5: 2 + 3 = 5. -/
```

## Source Excerpt

```lean
theorem generators_total_five :
    2 + 3 = (5 : Nat) := by omega
```
