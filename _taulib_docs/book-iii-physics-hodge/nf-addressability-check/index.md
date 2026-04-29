---
{
  "projection_kind": "taulib_declaration",
  "title": "nf_addressability_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-hodge/nf-addressability-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.Hodge`.",
  "declaration_id": "TauLib.BookIII.Physics.Hodge::nf_addressability_check",
  "declaration_slug": "nf-addressability-check",
  "kind": "def",
  "name": "nf_addressability_check",
  "module_name": "TauLib.BookIII.Physics.Hodge",
  "module_url": "/verify/taulib/docs/book-iii-physics-hodge/",
  "source_line_start": 165,
  "source_line_end": 170,
  "registry_ids": [
    "III.T28"
  ],
  "related_registry_items": [
    {
      "id": "III.T28",
      "title": "NF-Addressability Theorem",
      "url": "/registry/object/III.T28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L165-L170",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.Hodge",
        "url": "/verify/taulib/docs/book-iii-physics-hodge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L165-L170",
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

- Module: [TauLib.BookIII.Physics.Hodge](/verify/taulib/docs/book-iii-physics-hodge/)
- Source path: [`TauLib/BookIII/Physics/Hodge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L165-L170)
- Source range: L165-L170
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T28` — NF-Addressability Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T28] NF-addressability: every element of ℤ/Prim(k)ℤ is uniquely
    determined by its BNF triple. Combines BNF injectivity (from III.P16)
    and sector addressability (from III.D48). -/
```

## Source Excerpt

```lean
def nf_addressability_check (bound db : TauIdx) : Bool :=
  -- Sector addressability (surjective: every element has an address)
  let surj := sector_addressability_check bound db
  -- NF discreteness (injective: distinct elements have distinct addresses)
  let inj := nf_discreteness_check db
  surj && inj
```
