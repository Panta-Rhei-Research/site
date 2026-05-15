---
{
  "projection_kind": "taulib_declaration",
  "title": "TauInt.equiv_trans",
  "permalink": "/corpus/taulib/docs/book-i-boundary-number-tower/equiv-trans/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.NumberTower`.",
  "declaration_id": "TauLib.BookI.Boundary.NumberTower::TauInt.equiv_trans",
  "declaration_slug": "equiv-trans",
  "kind": "theorem",
  "name": "TauInt.equiv_trans",
  "module_name": "TauLib.BookI.Boundary.NumberTower",
  "module_url": "/corpus/taulib/docs/book-i-boundary-number-tower/",
  "source_line_start": 101,
  "source_line_end": 107,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean#L101-L107",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.NumberTower",
        "url": "/corpus/taulib/docs/book-i-boundary-number-tower/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean#L101-L107",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Boundary.NumberTower](/corpus/taulib/docs/book-i-boundary-number-tower/)
- Source path: [`TauLib/BookI/Boundary/NumberTower.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean#L101-L107)
- Source range: L101-L107
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- TauInt equivalence is transitive. -/
```

## Source Excerpt

```lean
theorem TauInt.equiv_trans {a b c : TauInt}
    (hab : TauInt.equiv a b) (hbc : TauInt.equiv b c) :
    TauInt.equiv a c := by
  show a.pos + c.neg = c.pos + a.neg
  have h1 : a.pos + b.neg = b.pos + a.neg := hab
  have h2 : b.pos + c.neg = c.pos + b.neg := hbc
  simp only [TauIdx] at *; omega
```
