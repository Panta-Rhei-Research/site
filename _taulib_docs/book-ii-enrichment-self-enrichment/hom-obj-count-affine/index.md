---
{
  "projection_kind": "taulib_declaration",
  "title": "hom_obj_count_affine",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/hom-obj-count-affine/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.SelfEnrichment`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfEnrichment::hom_obj_count_affine",
  "declaration_slug": "hom-obj-count-affine",
  "kind": "def",
  "name": "hom_obj_count_affine",
  "module_name": "TauLib.BookII.Enrichment.SelfEnrichment",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/",
  "source_line_start": 132,
  "source_line_end": 146,
  "registry_ids": [
    "II.D54"
  ],
  "related_registry_items": [
    {
      "id": "II.D54",
      "title": "Hom Object",
      "url": "/registry/object/II.D54/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L132-L146",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.SelfEnrichment",
        "url": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L132-L146",
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

- Module: [TauLib.BookII.Enrichment.SelfEnrichment](/verify/taulib/docs/book-ii-enrichment-self-enrichment/)
- Source path: [`TauLib/BookII/Enrichment/SelfEnrichment.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L132-L146)
- Source range: L132-L146
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D54` — Hom Object

## Immediate Comment / Docstring

```lean
/-- [II.D54] Hom object count at stage k: the number of reduce-compatible
    endomorphisms on Z/P_kZ. We enumerate all maps of the form
    x ↦ (a * x + b) mod P_k and count which are reduce-compatible.
    (Affine maps are a subset; the full count includes more, but these
    provide a lower bound.) -/
```

## Source Excerpt

```lean
def hom_obj_count_affine (k : TauIdx) : TauIdx :=
  let pk := primorial k
  if pk == 0 then 0
  else go pk 0 0 0 (pk * pk + 1)
where
  go (pk a b acc fuel : Nat) : Nat :=
    if fuel = 0 then acc
    else if a >= pk then acc
    else if b >= pk then go pk (a + 1) 0 acc (fuel - 1)
    else
      let f := fun x => reduce (a * x + b) k
      let compat := is_reduce_compat_at f k
      let new_acc := if compat then acc + 1 else acc
      go pk a (b + 1) new_acc (fuel - 1)
  termination_by fuel
```
