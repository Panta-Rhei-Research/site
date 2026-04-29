---
{
  "projection_kind": "taulib_declaration",
  "title": "OmegaGermApproach",
  "permalink": "/verify/taulib/docs/book-i-sets-unique-infinity/omega-germ-approach/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Sets.UniqueInfinity`.",
  "declaration_id": "TauLib.BookI.Sets.UniqueInfinity::OmegaGermApproach",
  "declaration_slug": "omega-germ-approach",
  "kind": "structure",
  "name": "OmegaGermApproach",
  "module_name": "TauLib.BookI.Sets.UniqueInfinity",
  "module_url": "/verify/taulib/docs/book-i-sets-unique-infinity/",
  "source_line_start": 59,
  "source_line_end": 68,
  "registry_ids": [
    "I.D76"
  ],
  "related_registry_items": [
    {
      "id": "I.D76",
      "title": "Omega-Germ Approach",
      "url": "/registry/object/I.D76/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L59-L68",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.UniqueInfinity",
        "url": "/verify/taulib/docs/book-i-sets-unique-infinity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L59-L68",
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

- Module: [TauLib.BookI.Sets.UniqueInfinity](/verify/taulib/docs/book-i-sets-unique-infinity/)
- Source path: [`TauLib/BookI/Sets/UniqueInfinity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L59-L68)
- Source range: L59-L68
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D76` — Omega-Germ Approach

## Immediate Comment / Docstring

```lean
/-- [I.D76] The Omega-Germ Approach: omega-germs are compatible towers
    on the primorial ladder, equipped with the divergence ultrametric.
    This replaces "set of all reals" with "inverse limit of finite rings."

    The approach has three components:
    1. The primorial ladder M_1 | M_2 | M_3 | ... provides the tower
    2. Reduction maps pi_{l->k} : Z/M_l -> Z/M_k give compatibility
    3. The divergence ultrametric measures agreement depth -/
```

## Source Excerpt

```lean
structure OmegaGermApproach where
  /-- The primorial ladder is well-defined: M_k > 0 for all k -/
  ladder_positive : forall k, primorial k > 0
  /-- The ladder is divisible: M_k | M_l for k <= l -/
  ladder_divisible : forall k l, k ≤ l -> primorial k ∣ primorial l
  /-- Reduction maps compose: (x mod M_l) mod M_k = x mod M_k for k <= l -/
  reduction_compatible : forall (x : TauIdx) (k l : TauIdx),
    k ≤ l -> reduce (reduce x l) k = reduce x k
  /-- The ultrametric is symmetric -/
  ultra_sym : forall (t1 t2 : OmegaTail), ultra_dist t1 t2 = ultra_dist t2 t1
```
