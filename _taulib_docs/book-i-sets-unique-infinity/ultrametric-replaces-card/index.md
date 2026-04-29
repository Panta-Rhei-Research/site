---
{
  "projection_kind": "taulib_declaration",
  "title": "ultrametric_replaces_card",
  "permalink": "/verify/taulib/docs/book-i-sets-unique-infinity/ultrametric-replaces-card/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.UniqueInfinity`.",
  "declaration_id": "TauLib.BookI.Sets.UniqueInfinity::ultrametric_replaces_card",
  "declaration_slug": "ultrametric-replaces-card",
  "kind": "theorem",
  "name": "ultrametric_replaces_card",
  "module_name": "TauLib.BookI.Sets.UniqueInfinity",
  "module_url": "/verify/taulib/docs/book-i-sets-unique-infinity/",
  "source_line_start": 177,
  "source_line_end": 187,
  "registry_ids": [
    "I.P37"
  ],
  "related_registry_items": [
    {
      "id": "I.P37",
      "title": "Ultrametric Replaces Cardinality",
      "url": "/registry/object/I.P37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L177-L187",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L177-L187",
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

- Module: [TauLib.BookI.Sets.UniqueInfinity](/verify/taulib/docs/book-i-sets-unique-infinity/)
- Source path: [`TauLib/BookI/Sets/UniqueInfinity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L177-L187)
- Source range: L177-L187
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P37` — Ultrametric Replaces Cardinality

## Immediate Comment / Docstring

```lean
/-- [I.P37] Ultrametric structure replaces cardinality hierarchy.

    In ZF, the chain aleph_0 < aleph_1 < aleph_2 < ... measures
    "how many" elements a set has. In tau, this hierarchy collapses:
    there is only one infinity (omega), and the notion of "size" is
    replaced by PROXIMITY in the divergence ultrametric.

    Two omega-tails are "close" if they agree to deep primorial depth,
    and "far" if they diverge early. This is an ultrametric (satisfies
    the strong triangle inequality), providing a finer structure than
    cardinality.

    The replacement has three pillars:
    1. The ultrametric exists (from OmegaGerms)
    2. It satisfies the strong triangle inequality (ultra_triangle)
    3. There is no second infinity to compare against (unique_infinity)

    We package these as a single theorem. -/
```

## Source Excerpt

```lean
theorem ultrametric_replaces_card :
    -- Pillar 1: ultrametric is well-defined
    (forall (t1 t2 : OmegaTail), ultra_dist t1 t2 = ultra_dist t2 t1) /\
    -- Pillar 2: strong triangle inequality (for equal-depth tails)
    (forall (t1 t2 t3 : OmegaTail),
      t1.depth = t2.depth -> t1.depth = t3.depth ->
      ultra_dist t1 t3 = 0 ∨
      ultra_dist t1 t3 ≥ Nat.min (ultra_dist t1 t2) (ultra_dist t2 t3)) /\
    -- Pillar 3: unique infinity (no cardinality hierarchy)
    (forall (x : TauObj), InfinityObject x -> x.seed = omega) :=
  ⟨ultra_symmetric, ultra_triangle, unique_infinity⟩
```
