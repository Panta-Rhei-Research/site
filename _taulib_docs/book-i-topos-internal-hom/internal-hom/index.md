---
{
  "projection_kind": "taulib_declaration",
  "title": "internal_hom",
  "permalink": "/verify/taulib/docs/book-i-topos-internal-hom/internal-hom/",
  "summary_short": "`def` declaration in `TauLib.BookI.Topos.InternalHom`.",
  "declaration_id": "TauLib.BookI.Topos.InternalHom::internal_hom",
  "declaration_slug": "internal-hom",
  "kind": "def",
  "name": "internal_hom",
  "module_name": "TauLib.BookI.Topos.InternalHom",
  "module_url": "/verify/taulib/docs/book-i-topos-internal-hom/",
  "source_line_start": 34,
  "source_line_end": 35,
  "registry_ids": [
    "I.D64"
  ],
  "related_registry_items": [
    {
      "id": "I.D64",
      "title": "Internal Hom",
      "url": "/registry/object/I.D64/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/InternalHom.lean#L34-L35",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.InternalHom",
        "url": "/verify/taulib/docs/book-i-topos-internal-hom/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/InternalHom.lean#L34-L35",
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

- Module: [TauLib.BookI.Topos.InternalHom](/verify/taulib/docs/book-i-topos-internal-hom/)
- Source path: [`TauLib/BookI/Topos/InternalHom.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/InternalHom.lean#L34-L35)
- Source range: L34-L35
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D64` — Internal Hom

## Immediate Comment / Docstring

```lean
/-- [I.D64] The internal hom Q^P: pointwise implication.
    (Q^P)(X) = true iff P(X) implies Q(X). -/
```

## Source Excerpt

```lean
def internal_hom (P Q : Presheaf) : Presheaf :=
  ⟨fun x => !P.support x || Q.support x⟩
```
