---
{
  "projection_kind": "taulib_declaration",
  "title": "NoShrinkStatement",
  "permalink": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/no-shrink-statement/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.NoShrinkExtended`.",
  "declaration_id": "TauLib.BookV.Cosmology.NoShrinkExtended::NoShrinkStatement",
  "declaration_slug": "no-shrink-statement",
  "kind": "structure",
  "name": "NoShrinkStatement",
  "module_name": "TauLib.BookV.Cosmology.NoShrinkExtended",
  "module_url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/",
  "source_line_start": 119,
  "source_line_end": 128,
  "registry_ids": [
    "V.T114"
  ],
  "related_registry_items": [
    {
      "id": "V.T114",
      "title": "No-Shrink Theorem",
      "url": "/registry/object/V.T114/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L119-L128",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.NoShrinkExtended",
        "url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L119-L128",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookV.Cosmology.NoShrinkExtended](/verify/taulib/docs/book-v-cosmology-no-shrink-extended/)
- Source path: [`TauLib/BookV/Cosmology/NoShrinkExtended.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L119-L128)
- Source range: L119-L128
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T114` — No-Shrink Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T114] No-shrink theorem: for any mature BH with M ≥ M_min,
    dM/dn ≥ 0. No τ-admissible evolution path reduces the mass.

    This is the τ-analogue of the classical area theorem (Hawking 1971),
    but stronger: it applies to the MASS (not just area), and it is
    exact (not just semiclassical).

    Structural proof: mass decrease would create defect cost (V.T113),
    but the mature BH has minimum defect (zero). Therefore mass
    cannot decrease. -/
```

## Source Excerpt

```lean
structure NoShrinkStatement where
  /-- The mature BH. -/
  mbh : MatureBlackHole
  /-- Mass at tick n. -/
  mass_n : Nat
  /-- Mass at tick n+1. -/
  mass_n_plus_1 : Nat
  /-- No-shrink: mass doesn't decrease. -/
  no_shrink : mass_n_plus_1 ≥ mass_n
  deriving Repr
```
