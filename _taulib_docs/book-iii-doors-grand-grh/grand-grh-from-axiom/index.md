---
{
  "projection_kind": "taulib_declaration",
  "title": "grand_grh_from_axiom",
  "permalink": "/verify/taulib/docs/book-iii-doors-grand-grh/grand-grh-from-axiom/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.GrandGRH`.",
  "declaration_id": "TauLib.BookIII.Doors.GrandGRH::grand_grh_from_axiom",
  "declaration_slug": "grand-grh-from-axiom",
  "kind": "theorem",
  "name": "grand_grh_from_axiom",
  "module_name": "TauLib.BookIII.Doors.GrandGRH",
  "module_url": "/verify/taulib/docs/book-iii-doors-grand-grh/",
  "source_line_start": 250,
  "source_line_end": 254,
  "registry_ids": [
    "III.D31"
  ],
  "related_registry_items": [
    {
      "id": "III.D31",
      "title": "Grand GRH (τ-effective)",
      "url": "/registry/object/III.D31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L250-L254",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.GrandGRH",
        "url": "/verify/taulib/docs/book-iii-doors-grand-grh/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L250-L254",
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

- Module: [TauLib.BookIII.Doors.GrandGRH](/verify/taulib/docs/book-iii-doors-grand-grh/)
- Source path: [`TauLib/BookIII/Doors/GrandGRH.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L250-L254)
- Source range: L250-L254
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D31` — Grand GRH (τ-effective)

## Immediate Comment / Docstring

```lean
/-- [III.D31] Structural: Grand GRH from axiom. -/
```

## Source Excerpt

```lean
theorem grand_grh_from_axiom (k : Nat) :
    grand_grh_finite_check k = true :=
  grand_grh_adelic k

end Tau.BookIII.Doors
```
