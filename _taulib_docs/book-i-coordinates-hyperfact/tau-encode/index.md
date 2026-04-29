---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_encode",
  "permalink": "/verify/taulib/docs/book-i-coordinates-hyperfact/tau-encode/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.Hyperfact`.",
  "declaration_id": "TauLib.BookI.Coordinates.Hyperfact::tau_encode",
  "declaration_slug": "tau-encode",
  "kind": "def",
  "name": "tau_encode",
  "module_name": "TauLib.BookI.Coordinates.Hyperfact",
  "module_url": "/verify/taulib/docs/book-i-coordinates-hyperfact/",
  "source_line_start": 78,
  "source_line_end": 79,
  "registry_ids": [
    "I.C01"
  ],
  "related_registry_items": [
    {
      "id": "I.C01",
      "title": "Constructive Encoding via ABCD",
      "url": "/registry/object/I.C01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Hyperfact.lean#L78-L79",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.Hyperfact",
        "url": "/verify/taulib/docs/book-i-coordinates-hyperfact/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Hyperfact.lean#L78-L79",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookI.Coordinates.Hyperfact](/verify/taulib/docs/book-i-coordinates-hyperfact/)
- Source path: [`TauLib/BookI/Coordinates/Hyperfact.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Hyperfact.lean#L78-L79)
- Source range: L78-L79
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.C01` — Constructive Encoding via ABCD

## Immediate Comment / Docstring

```lean
/-- [I.C01] Encoding: map X to its (spine, final remainder) pair.
    This is injective by the Hyperfactorization Theorem. -/
```

## Source Excerpt

```lean
def tau_encode (x : TauIdx) : List (TauIdx × TauIdx × TauIdx) × TauIdx :=
  (spine x, if x ≤ 1 then x else 1)
```
